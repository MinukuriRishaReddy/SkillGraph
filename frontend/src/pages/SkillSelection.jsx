import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import Box from '@mui/material/Box';
import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import CircularProgress from '@mui/material/CircularProgress';
import Alert from '@mui/material/Alert';
import Stepper from '@mui/material/Stepper';
import Step from '@mui/material/Step';
import StepLabel from '@mui/material/StepLabel';
import ArrowForwardIcon from '@mui/icons-material/ArrowForward';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import SkillSelector from '../components/SkillSelector';
import {
  getLanguages,
  getKnowledge,
  getTools,
  getFrameworks,
  getPlatforms,
  submitUserSkills,
} from '../api/api';

const STEPS = ['Select Career', 'Choose Skills', 'View Learning Path'];

const CATEGORIES = [
  { key: 'languages', label: 'Programming Languages', fetcher: getLanguages, color: 'primary' },
  { key: 'knowledge', label: 'Knowledge & Concepts', fetcher: getKnowledge, color: 'secondary' },
  { key: 'tools', label: 'Tools', fetcher: getTools, color: 'success' },
  { key: 'frameworks', label: 'Frameworks', fetcher: getFrameworks, color: 'info' },
  { key: 'platforms', label: 'Platforms', fetcher: getPlatforms, color: 'warning' },
];

const TYPE_MAP = {
  languages: 'ProgramingLanguage',
  knowledge: 'Knowledge',
  tools: 'Tool',
  frameworks: 'Framework',
  platforms: 'Platform',
};

export default function SkillSelection() {
  const navigate = useNavigate();
  const userId = localStorage.getItem('userId');
  const [skills, setSkills] = useState({});
  const [selectedIds, setSelectedIds] = useState([]);
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    if (!userId) {
      navigate('/login');
      return;
    }

    const loadSkills = async () => {
      try {
        const results = await Promise.all(CATEGORIES.map((c) => c.fetcher()));
        const data = {};
        CATEGORIES.forEach((cat, i) => {
          data[cat.key] = results[i].data || [];
        });
        setSkills(data);
      } catch (err) {
        setError(err.response?.data?.error || 'Failed to load skills');
      } finally {
        setLoading(false);
      }
    };
    loadSkills();
  }, [userId, navigate]);

  const toggleSkill = (id) => {
    setSelectedIds((prev) =>
      prev.includes(id) ? prev.filter((x) => x !== id) : [...prev, id]
    );
  };

  const findSkillCategory = (id) => {
    for (const cat of CATEGORIES) {
      if (skills[cat.key]?.some((s) => s.id === id)) {
        return cat.key;
      }
    }
    return 'knowledge';
  };

  const handleSubmit = async () => {
    setSubmitting(true);
    setError('');
    try {
      const listLo = selectedIds.map((id) => ({
        id,
        type: TYPE_MAP[findSkillCategory(id)] || 'Knowledge',
        level: 1,
      }));
      await submitUserSkills(Number(userId), listLo);
      navigate('/learning-path');
    } catch (err) {
      setError(err.response?.data?.error || 'Failed to save skills');
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <Box sx={{ bgcolor: 'grey.50', minHeight: 'calc(100vh - 64px)', py: 4 }}>
      <Container maxWidth="md">
        <Stepper activeStep={1} alternativeLabel sx={{ mb: 4 }}>
          {STEPS.map((label) => (
            <Step key={label}>
              <StepLabel>{label}</StepLabel>
            </Step>
          ))}
        </Stepper>

        <Typography variant="h4" fontWeight={700} gutterBottom>
          Select Your Skills
        </Typography>
        <Typography variant="body1" color="text.secondary" sx={{ mb: 3 }}>
          Choose the skills you already have. This helps us identify what you need to learn.
        </Typography>

        {error && (
          <Alert severity="error" sx={{ mb: 2 }} onClose={() => setError('')}>
            {error}
          </Alert>
        )}

        {loading ? (
          <Box sx={{ display: 'flex', justifyContent: 'center', py: 8 }}>
            <CircularProgress />
          </Box>
        ) : (
          <>
            {CATEGORIES.map((cat) => (
              <SkillSelector
                key={cat.key}
                title={cat.label}
                skills={skills[cat.key] || []}
                selectedIds={selectedIds}
                onToggle={toggleSkill}
                color={cat.color}
              />
            ))}

            <Box sx={{ display: 'flex', justifyContent: 'space-between', mt: 3 }}>
              <Button
                variant="outlined"
                startIcon={<ArrowBackIcon />}
                onClick={() => navigate('/careers')}
              >
                Back
              </Button>
              <Button
                variant="contained"
                size="large"
                onClick={handleSubmit}
                disabled={submitting}
                endIcon={
                  submitting ? (
                    <CircularProgress size={20} color="inherit" />
                  ) : (
                    <ArrowForwardIcon />
                  )
                }
              >
                Generate Learning Path ({selectedIds.length} skills selected)
              </Button>
            </Box>
          </>
        )}
      </Container>
    </Box>
  );
}
