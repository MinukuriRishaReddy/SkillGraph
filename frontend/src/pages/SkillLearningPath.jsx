import { useState, useEffect, useCallback } from 'react';
import { useNavigate } from 'react-router-dom';
import Box from '@mui/material/Box';
import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';
import CircularProgress from '@mui/material/CircularProgress';
import Alert from '@mui/material/Alert';
import Button from '@mui/material/Button';
import Paper from '@mui/material/Paper';
import IconButton from '@mui/material/IconButton';
import Tooltip from '@mui/material/Tooltip';
import RefreshIcon from '@mui/icons-material/Refresh';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import AccountTreeIcon from '@mui/icons-material/AccountTree';
import SkillGraphView from '../components/SkillGraphView';
import Chatbot from '../components/Chatbot';
import { getSkillLearningPath, getUserInfo, getUserSkills } from '../api/api';

export default function SkillLearningPath() {
  const navigate = useNavigate();
  const userId = localStorage.getItem('userId');
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  const loadGraph = useCallback(async () => {
    if (!userId) {
      navigate('/login');
      return;
    }
    setLoading(true);
    setError('');
    setData(null);

    try {
      // Get user's career objective
      const userRes = await getUserInfo(userId);
      const careerId = userRes.data?.career?.id;
      if (!careerId) {
        setError('No career goal set. Please select a career first.');
        setLoading(false);
        return;
      }

      // Fetch skill learning path and user's existing skills in parallel
      const [{ data: pathData }, skillsRes] = await Promise.all([
        getSkillLearningPath(careerId),
        getUserSkills(userId),
      ]);
      if (!pathData || !pathData.skills || pathData.skills.length === 0) {
        setError('No skills found for this career path.');
        setLoading(false);
        return;
      }
      // Build a Set of user's skill IDs (convert to string to match graph IDs)
      const userSkillIds = new Set(
        (skillsRes.data || []).map((s) => String(s.id))
      );
      setData({ ...pathData, userSkillIds });
    } catch (err) {
      setError(err.response?.data?.error || 'Failed to load skill learning path.');
    } finally {
      setLoading(false);
    }
  }, [userId, navigate]);

  useEffect(() => {
    loadGraph();
  }, [loadGraph]);

  return (
    <Box sx={{ bgcolor: 'grey.50', minHeight: 'calc(100vh - 64px)', py: 4 }}>
      <Container maxWidth="lg">
        {/* Header */}
        <Box sx={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', mb: 3 }}>
          <Box sx={{ display: 'flex', alignItems: 'center', gap: 2 }}>
            <AccountTreeIcon sx={{ fontSize: 36, color: 'primary.main' }} />
            <Box>
              <Typography variant="h4" fontWeight={700}>
                Skill Learning Path
              </Typography>
              <Typography variant="body1" color="text.secondary">
                {data
                  ? `${data.career} - Click skills to mark progress`
                  : 'Interactive skill dependency graph'}
              </Typography>
            </Box>
          </Box>
          <Box sx={{ display: 'flex', gap: 1 }}>
            <Tooltip title="Back to Learning Path">
              <IconButton onClick={() => navigate('/learning-path')}>
                <ArrowBackIcon />
              </IconButton>
            </Tooltip>
            <Tooltip title="Refresh">
              <span>
                <IconButton onClick={loadGraph} disabled={loading}>
                  <RefreshIcon />
                </IconButton>
              </span>
            </Tooltip>
          </Box>
        </Box>

        {error && (
          <Alert
            severity="warning"
            sx={{ mb: 2 }}
            action={
              <Button color="inherit" size="small" onClick={() => navigate('/careers')}>
                Setup Path
              </Button>
            }
          >
            {error}
          </Alert>
        )}

        {loading ? (
          <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center', py: 8 }}>
            <CircularProgress size={48} sx={{ mb: 2 }} />
            <Typography color="text.secondary">Loading skill graph...</Typography>
          </Box>
        ) : data ? (
          <Paper variant="outlined" sx={{ p: 3 }}>
            <SkillGraphView
              skills={data.skills}
              relations={data.relations}
              career={data.career}
              userSkillIds={data.userSkillIds}
            />
          </Paper>
        ) : null}

        {/* Actions */}
        {!loading && (
          <Box
            sx={{
              display: 'flex',
              justifyContent: 'space-between',
              alignItems: 'center',
              mt: 3,
              pr: { xs: 0, sm: '80px' }, // Add padding on the right to avoid chatbot overlap
            }}
          >
            <Button variant="outlined" onClick={() => navigate('/learning-path')}>
              Course View
            </Button>
            <Button variant="outlined" onClick={() => navigate('/careers')}>
              Change Career
            </Button>
          </Box>
        )}
      </Container>
      <Chatbot />
    </Box>
  );
}
