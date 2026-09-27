import { useState, useEffect, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import Box from '@mui/material/Box';
import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import CircularProgress from '@mui/material/CircularProgress';
import Alert from '@mui/material/Alert';
import Grid from '@mui/material/Grid';
import Stepper from '@mui/material/Stepper';
import Step from '@mui/material/Step';
import StepLabel from '@mui/material/StepLabel';
import ArrowForwardIcon from '@mui/icons-material/ArrowForward';
import CareerCard from '../components/CareerCard';
import { getAllCareers, setUserObjective } from '../api/api';

const STEPS = ['Select Career', 'Choose Skills', 'View Learning Path'];

export default function CareerSelection() {
  const navigate = useNavigate();
  const userId = localStorage.getItem('userId');
  const [careers, setCareers] = useState([]);
  const [selectedId, setSelectedId] = useState(null);
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState('');
  const continueRef = useRef(null);

  useEffect(() => {
    if (!userId) {
      navigate('/login');
      return;
    }
    getAllCareers()
      .then(({ data }) => setCareers(data))
      .catch((err) => setError(err.response?.data?.error || 'Failed to load careers'))
      .finally(() => setLoading(false));
  }, [userId, navigate]);

  const handleCareerSelect = (id) => {
    setSelectedId(id);
    // Smooth scroll to the continue button container
    setTimeout(() => {
      continueRef.current?.scrollIntoView({
        behavior: 'smooth',
        block: 'center',
      });
    }, 200);
  };

  const handleContinue = async () => {
    if (!selectedId) return;
    setSubmitting(true);
    setError('');
    try {
      await setUserObjective(Number(userId), selectedId);
      navigate('/skills');
    } catch (err) {
      setError(err.response?.data?.error || 'Failed to set career objective');
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <Box sx={{ bgcolor: 'grey.50', minHeight: 'calc(100vh - 64px)', py: 4 }}>
      <Container maxWidth="md">
        <Stepper activeStep={0} alternativeLabel sx={{ mb: 4 }}>
          {STEPS.map((label) => (
            <Step key={label}>
              <StepLabel>{label}</StepLabel>
            </Step>
          ))}
        </Stepper>

        <Typography variant="h4" fontWeight={700} gutterBottom>
          Choose Your Career Goal
        </Typography>
        <Typography variant="body1" color="text.secondary" sx={{ mb: 3 }}>
          Select the career path you want to pursue. We&apos;ll create a personalized learning roadmap for you.
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
            <Grid container spacing={2} sx={{ mb: 3 }}>
              {careers.map((career) => (
                <Grid item xs={12} sm={6} key={career.id}>
                  <CareerCard
                    career={career}
                    selected={selectedId === career.id}
                    onClick={() => handleCareerSelect(career.id)}
                  />
                </Grid>
              ))}
            </Grid>

            {careers.length === 0 && !error && (
              <Typography color="text.secondary" textAlign="center" sx={{ py: 4 }}>
                No careers available at the moment.
              </Typography>
            )}

            <Box ref={continueRef} sx={{ display: 'flex', justifyContent: 'flex-end', pt: 2 }}>
              <Button
                variant="contained"
                size="large"
                onClick={handleContinue}
                disabled={!selectedId || submitting}
                endIcon={submitting ? <CircularProgress size={20} color="inherit" /> : <ArrowForwardIcon />}
              >
                Continue to Skills
              </Button>
            </Box>
          </>
        )}
      </Container>
    </Box>
  );
}
