import { useState, useEffect, useCallback } from 'react';
import { useNavigate } from 'react-router-dom';
import Box from '@mui/material/Box';
import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import CircularProgress from '@mui/material/CircularProgress';
import Alert from '@mui/material/Alert';
import Paper from '@mui/material/Paper';
import Stepper from '@mui/material/Stepper';
import Step from '@mui/material/Step';
import StepLabel from '@mui/material/StepLabel';
import Tabs from '@mui/material/Tabs';
import Tab from '@mui/material/Tab';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import Chip from '@mui/material/Chip';
import Divider from '@mui/material/Divider';
import IconButton from '@mui/material/IconButton';
import Tooltip from '@mui/material/Tooltip';
import RefreshIcon from '@mui/icons-material/Refresh';
import DownloadIcon from '@mui/icons-material/Download';
import ListAltIcon from '@mui/icons-material/ListAlt';
import AccountTreeIcon from '@mui/icons-material/AccountTree';
import CheckCircleOutlineIcon from '@mui/icons-material/CheckCircleOutline';
import OpenInNewIcon from '@mui/icons-material/OpenInNew';
import AccessTimeIcon from '@mui/icons-material/AccessTime';
import AttachMoneyIcon from '@mui/icons-material/AttachMoney';
import StarIcon from '@mui/icons-material/Star';
import PeopleIcon from '@mui/icons-material/People';
import BubbleChartIcon from '@mui/icons-material/BubbleChart';
import GraphView from '../components/GraphView';
import {
  getLearningPath,
  getCourseInfo,
  getLearningPathInfo,
  getCourseProvidedLOs,
} from '../api/api';

const STEPS = ['Select Career', 'Choose Skills', 'View Learning Path'];

export default function LearningPath() {
  const navigate = useNavigate();
  const userId = localStorage.getItem('userId');
  const [paths, setPaths] = useState([]);
  const [courses, setCourses] = useState([]);
  const [pathInfo, setPathInfo] = useState(null);
  const [selectedPathIdx, setSelectedPathIdx] = useState(0);
  const [tabValue, setTabValue] = useState(0);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  const loadPath = useCallback(async () => {
    if (!userId) {
      navigate('/login');
      return;
    }
    setLoading(true);
    setError('');
    setCourses([]);
    setPathInfo(null);

    try {
      const { data } = await getLearningPath(userId);
      if (!data || data.length === 0) {
        setError('No learning path generated. Please select a career and skills first.');
        setLoading(false);
        return;
      }
      setPaths(data);

      // Load course details for the first path
      const firstPath = data[0];
      const rawPath = firstPath.path || firstPath;
      // path is an array of sub-paths (e.g. [[109,110],[77,79]]) — flatten to a single list
      const courseIds = rawPath.flat();
      await loadCourseDetails(courseIds, Number(userId));
    } catch (err) {
      setError(err.response?.data?.error || 'Failed to generate learning path');
    } finally {
      setLoading(false);
    }
  }, [userId, navigate]);

  const loadCourseDetails = async (courseIds, uid) => {
    try {
      // Fetch course info for each course in the path
      const coursePromises = courseIds.map((id) => getCourseInfo(id).catch(() => null));
      const courseResults = await Promise.all(coursePromises);
      const coursesData = courseResults
        .filter(Boolean)
        .map((r) => r.data);

      // Fetch provided LOs for each course
      const loPromises = courseIds.map((id) => getCourseProvidedLOs(id).catch(() => ({ data: [] })));
      const loResults = await Promise.all(loPromises);

      const enrichedCourses = coursesData.map((course, i) => ({
        ...course,
        provides: loResults[i]?.data || [],
      }));

      setCourses(enrichedCourses);

      // Get path summary info
      try {
        const infoRes = await getLearningPathInfo(courseIds, uid);
        setPathInfo(infoRes.data);
      } catch {
        // Path info is optional
      }
    } catch {
      // Course details are optional; we still show the path
    }
  };

  useEffect(() => {
    loadPath();
  }, [loadPath]);

  const handlePathChange = async (idx) => {
    setSelectedPathIdx(idx);
    const pathData = paths[idx];
    const rawPath = pathData.path || pathData;
    const courseIds = rawPath.flat();
    setCourses([]);
    setPathInfo(null);
    await loadCourseDetails(courseIds, Number(userId));
  };

  const handleDownload = () => {
    const text = courses
      .map((c, i) => `${i + 1}. ${c.name}${c.link ? ` - ${c.link}` : ''}`)
      .join('\n');
    const summary = pathInfo
      ? `\n\nSummary:\n- Courses: ${pathInfo.course}\n- Estimated Time: ${pathInfo.time} hours\n- Estimated Cost: $${pathInfo.cost}`
      : '';
    const blob = new Blob([`Learning Path\n${'='.repeat(40)}\n\n${text}${summary}`], {
      type: 'text/plain',
    });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'learning-path.txt';
    a.click();
    URL.revokeObjectURL(url);
  };

  return (
    <Box sx={{ bgcolor: 'grey.50', minHeight: 'calc(100vh - 64px)', py: 4 }}>
      <Container maxWidth="lg">
        <Stepper activeStep={2} alternativeLabel sx={{ mb: 4 }}>
          {STEPS.map((label) => (
            <Step key={label}>
              <StepLabel>{label}</StepLabel>
            </Step>
          ))}
        </Stepper>

        <Box sx={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', mb: 2 }}>
          <Box>
            <Typography variant="h4" fontWeight={700}>
              Your Learning Path
            </Typography>
            <Typography variant="body1" color="text.secondary">
              Follow this roadmap to reach your career goal
            </Typography>
          </Box>
          <Box>
            <Tooltip title="Refresh">
              <span>
                <IconButton onClick={loadPath} disabled={loading}>
                  <RefreshIcon />
                </IconButton>
              </span>
            </Tooltip>
            {courses.length > 0 && (
              <Tooltip title="Download as text">
                <IconButton onClick={handleDownload}>
                  <DownloadIcon />
                </IconButton>
              </Tooltip>
            )}
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
            <Typography color="text.secondary">Generating your learning path...</Typography>
          </Box>
        ) : (
          <>
            {/* Path selector when multiple paths */}
            {paths.length > 1 && (
              <Paper variant="outlined" sx={{ p: 2, mb: 2 }}>
                <Typography variant="subtitle2" gutterBottom>
                  Available paths ({paths.length}):
                </Typography>
                <Box sx={{ display: 'flex', gap: 1, flexWrap: 'wrap' }}>
                  {paths.map((_, i) => (
                    <Chip
                      key={i}
                      label={`Path ${i + 1}`}
                      color={selectedPathIdx === i ? 'primary' : 'default'}
                      variant={selectedPathIdx === i ? 'filled' : 'outlined'}
                      onClick={() => handlePathChange(i)}
                    />
                  ))}
                </Box>
              </Paper>
            )}

            {/* Summary cards */}
            {pathInfo && (
              <Box sx={{ display: 'flex', gap: 2, mb: 3, flexWrap: 'wrap' }}>
                {[
                  { icon: <ListAltIcon />, label: 'Courses', value: pathInfo.course },
                  { icon: <AccessTimeIcon />, label: 'Est. Time', value: `${pathInfo.time}h` },
                  { icon: <AttachMoneyIcon />, label: 'Est. Cost', value: `$${pathInfo.cost}` },
                ].map((stat) => (
                  <Paper
                    key={stat.label}
                    variant="outlined"
                    sx={{ p: 2, display: 'flex', alignItems: 'center', gap: 1.5, flex: 1, minWidth: 160 }}
                  >
                    <Box sx={{ color: 'primary.main' }}>{stat.icon}</Box>
                    <Box>
                      <Typography variant="caption" color="text.secondary">
                        {stat.label}
                      </Typography>
                      <Typography variant="h6" fontWeight={700}>
                        {stat.value}
                      </Typography>
                    </Box>
                  </Paper>
                ))}
              </Box>
            )}

            {/* Tabs: List / Graph */}
            {courses.length > 0 && (
              <>
                <Paper variant="outlined" sx={{ mb: 3 }}>
                  <Tabs
                    value={tabValue}
                    onChange={(_, v) => setTabValue(v)}
                    sx={{ borderBottom: 1, borderColor: 'divider' }}
                  >
                    <Tab icon={<ListAltIcon />} label="Course List" iconPosition="start" />
                    <Tab icon={<AccountTreeIcon />} label="Graph View" iconPosition="start" />
                  </Tabs>

                  {tabValue === 0 && (
                    <List sx={{ p: 0 }}>
                      {courses.map((course, idx) => (
                        <Box key={course.id || idx}>
                          {idx > 0 && <Divider />}
                          <ListItem
                            sx={{ py: 2, px: 3 }}
                            secondaryAction={
                              course.link ? (
                                <Tooltip title="Open course">
                                  <IconButton
                                    edge="end"
                                    href={course.link}
                                    target="_blank"
                                    rel="noopener noreferrer"
                                  >
                                    <OpenInNewIcon />
                                  </IconButton>
                                </Tooltip>
                              ) : null
                            }
                          >
                            <ListItemIcon>
                              <Box
                                sx={{
                                  width: 36,
                                  height: 36,
                                  borderRadius: '50%',
                                  bgcolor: 'primary.main',
                                  color: '#fff',
                                  display: 'flex',
                                  alignItems: 'center',
                                  justifyContent: 'center',
                                  fontWeight: 700,
                                  fontSize: 14,
                                }}
                              >
                                {idx + 1}
                              </Box>
                            </ListItemIcon>
                            <ListItemText
                              primary={
                                <Typography fontWeight={600}>
                                  {course.name}
                                </Typography>
                              }
                              secondary={
                                <Box sx={{ display: 'flex', gap: 2, mt: 0.5, flexWrap: 'wrap' }}>
                                  {course.rating != null && (
                                    <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.3 }}>
                                      <StarIcon sx={{ fontSize: 16, color: 'warning.main' }} />
                                      <Typography variant="caption">{course.rating}</Typography>
                                    </Box>
                                  )}
                                  {course.time != null && (
                                    <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.3 }}>
                                      <AccessTimeIcon sx={{ fontSize: 16 }} />
                                      <Typography variant="caption">{course.time}h</Typography>
                                    </Box>
                                  )}
                                  {course.cost != null && (
                                    <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.3 }}>
                                      <AttachMoneyIcon sx={{ fontSize: 16 }} />
                                      <Typography variant="caption">{course.cost}</Typography>
                                    </Box>
                                  )}
                                  {course.enroll != null && (
                                    <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.3 }}>
                                      <PeopleIcon sx={{ fontSize: 16 }} />
                                      <Typography variant="caption">
                                        {course.enroll.toLocaleString()} enrolled
                                      </Typography>
                                    </Box>
                                  )}
                                  {course.provides?.length > 0 && (
                                    <Box sx={{ display: 'flex', gap: 0.5, flexWrap: 'wrap' }}>
                                      {course.provides.slice(0, 4).map((lo, j) => (
                                        <Chip
                                          key={j}
                                          size="small"
                                          icon={<CheckCircleOutlineIcon />}
                                          label={lo.name || lo.value}
                                          variant="outlined"
                                          color="success"
                                          sx={{ height: 22, fontSize: 11 }}
                                        />
                                      ))}
                                      {course.provides.length > 4 && (
                                        <Chip
                                          size="small"
                                          label={`+${course.provides.length - 4} more`}
                                          sx={{ height: 22, fontSize: 11 }}
                                        />
                                      )}
                                    </Box>
                                  )}
                                </Box>
                              }
                            />
                          </ListItem>
                        </Box>
                      ))}
                    </List>
                  )}

                  {tabValue === 1 && (
                    <Box sx={{ p: 2 }}>
                      <GraphView courses={courses} />
                    </Box>
                  )}
                </Paper>
              </>
            )}

            {/* Actions */}
            <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <Button variant="outlined" onClick={() => navigate('/skills')}>
                Update Skills
              </Button>
              <Button
                variant="contained"
                startIcon={<BubbleChartIcon />}
                onClick={() => navigate('/skill-path')}
              >
                Skill Graph
              </Button>
              <Button variant="outlined" onClick={() => navigate('/careers')}>
                Change Career
              </Button>
            </Box>
          </>
        )}
      </Container>
    </Box>
  );
}
