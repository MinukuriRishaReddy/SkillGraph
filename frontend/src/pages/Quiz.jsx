import { useState, useMemo } from 'react';
import { useSearchParams, useNavigate } from 'react-router-dom';
import confetti from 'canvas-confetti';
import Box from '@mui/material/Box';
import Container from '@mui/material/Container';
import Paper from '@mui/material/Paper';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import RadioGroup from '@mui/material/RadioGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import Radio from '@mui/material/Radio';
import LinearProgress from '@mui/material/LinearProgress';
import Alert from '@mui/material/Alert';
import Chip from '@mui/material/Chip';
import CheckCircleIcon from '@mui/icons-material/CheckCircle';
import CancelIcon from '@mui/icons-material/Cancel';
import EmojiEventsIcon from '@mui/icons-material/EmojiEvents';
import ReplayIcon from '@mui/icons-material/Replay';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import ArrowForwardIcon from '@mui/icons-material/ArrowForward';
import quizQuestions from '../data/quizQuestions';

const PASS_THRESHOLD = 7;

export default function Quiz() {
  const [searchParams] = useSearchParams();
  const navigate = useNavigate();
  const career = searchParams.get('career') || '';

  const questions = useMemo(() => quizQuestions[career] || [], [career]);

  const [currentIndex, setCurrentIndex] = useState(0);
  const [answers, setAnswers] = useState({});
  const [submitted, setSubmitted] = useState(false);

  if (!career || questions.length === 0) {
    return (
      <Box sx={{ minHeight: 'calc(100vh - 64px)', bgcolor: 'grey.50', py: 6 }}>
        <Container maxWidth="sm">
          <Paper sx={{ p: 4, textAlign: 'center' }}>
            <Typography variant="h5" gutterBottom>
              Quiz Not Available
            </Typography>
            <Typography color="text.secondary" sx={{ mb: 3 }}>
              No quiz found for "{career}". Please navigate from your learning path.
            </Typography>
            <Button variant="contained" onClick={() => navigate('/skill-path')}>
              Go to Learning Path
            </Button>
          </Paper>
        </Container>
      </Box>
    );
  }

  const score = questions.reduce(
    (acc, q, i) => acc + (answers[i] === q.correctAnswer ? 1 : 0),
    0
  );
  const passed = score >= PASS_THRESHOLD;
  const progress = ((currentIndex + 1) / questions.length) * 100;
  const allAnswered = questions.every((_, i) => answers[i] !== undefined);
  const currentQuestion = questions[currentIndex];

  const handleAnswer = (value) => {
    setAnswers((prev) => ({ ...prev, [currentIndex]: parseInt(value, 10) }));
  };

  const handleSubmit = () => {
    setSubmitted(true);
    const finalScore = questions.reduce(
      (acc, q, i) => acc + (answers[i] === q.correctAnswer ? 1 : 0),
      0
    );
    if (finalScore >= PASS_THRESHOLD) {
      confetti({
        particleCount: 150,
        spread: 80,
        origin: { x: 0.5, y: 0.5 },
        colors: ['#2e7d32', '#f9a825', '#1976d2', '#9c27b0', '#ff9800'],
      });
    }
  };

  const handleRetake = () => {
    setAnswers({});
    setCurrentIndex(0);
    setSubmitted(false);
  };

  // Results view
  if (submitted) {
    return (
      <Box sx={{ minHeight: 'calc(100vh - 64px)', bgcolor: 'grey.50', py: 6 }}>
        <Container maxWidth="md">
          <Paper sx={{ p: 4 }}>
            <Box sx={{ textAlign: 'center', mb: 4 }}>
              <Typography variant="h4" fontWeight={700} gutterBottom>
                Quiz Results
              </Typography>
              <Typography variant="h6" color="text.secondary" gutterBottom>
                {career}
              </Typography>

              <Box
                sx={{
                  display: 'inline-flex',
                  alignItems: 'center',
                  gap: 1,
                  bgcolor: passed ? 'success.50' : 'error.50',
                  border: '2px solid',
                  borderColor: passed ? 'success.main' : 'error.main',
                  borderRadius: 3,
                  px: 4,
                  py: 2,
                  my: 2,
                }}
              >
                {passed ? (
                  <EmojiEventsIcon sx={{ fontSize: 40, color: 'warning.main' }} />
                ) : (
                  <CancelIcon sx={{ fontSize: 40, color: 'error.main' }} />
                )}
                <Typography variant="h3" fontWeight={700} color={passed ? 'success.main' : 'error.main'}>
                  {score} / {questions.length}
                </Typography>
              </Box>

              {passed ? (
                <Alert severity="success" sx={{ mt: 2, justifyContent: 'center' }}>
                  Congratulations! You passed the quiz! Download your certificate below.
                </Alert>
              ) : (
                <Alert severity="error" sx={{ mt: 2, justifyContent: 'center' }}>
                  You need {PASS_THRESHOLD}+ correct answers to pass. Keep learning and try again!
                </Alert>
              )}
            </Box>

            {/* Question review */}
            <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2, mb: 4 }}>
              {questions.map((q, i) => {
                const isCorrect = answers[i] === q.correctAnswer;
                return (
                  <Paper
                    key={i}
                    variant="outlined"
                    sx={{
                      p: 2,
                      borderColor: isCorrect ? 'success.main' : 'error.main',
                      borderWidth: 2,
                      bgcolor: isCorrect ? 'success.50' : 'error.50',
                    }}
                  >
                    <Box sx={{ display: 'flex', alignItems: 'flex-start', gap: 1 }}>
                      {isCorrect ? (
                        <CheckCircleIcon color="success" sx={{ mt: 0.3 }} />
                      ) : (
                        <CancelIcon color="error" sx={{ mt: 0.3 }} />
                      )}
                      <Box>
                        <Typography variant="body2" fontWeight={600}>
                          Q{i + 1}: {q.question}
                        </Typography>
                        <Typography variant="body2" color="text.secondary">
                          Your answer: {q.options[answers[i]] || 'Not answered'}
                        </Typography>
                        {!isCorrect && (
                          <Typography variant="body2" color="success.dark" fontWeight={500}>
                            Correct answer: {q.options[q.correctAnswer]}
                          </Typography>
                        )}
                      </Box>
                    </Box>
                  </Paper>
                );
              })}
            </Box>

            {/* Action buttons */}
            <Box sx={{ display: 'flex', gap: 2, justifyContent: 'center' }}>
              {passed ? (
                <Button
                  variant="contained"
                  size="large"
                  startIcon={<EmojiEventsIcon />}
                  onClick={() => navigate(`/certificate?career=${encodeURIComponent(career)}`)}
                >
                  Download Certificate
                </Button>
              ) : (
                <Button
                  variant="contained"
                  size="large"
                  startIcon={<ReplayIcon />}
                  onClick={handleRetake}
                >
                  Retake Quiz
                </Button>
              )}
              <Button
                variant="outlined"
                size="large"
                onClick={() => navigate('/skill-path')}
              >
                Back to Learning Path
              </Button>
            </Box>
          </Paper>
        </Container>
      </Box>
    );
  }

  // Quiz view
  return (
    <Box sx={{ minHeight: 'calc(100vh - 64px)', bgcolor: 'grey.50', py: 6 }}>
      <Container maxWidth="md">
        <Paper sx={{ p: 4 }}>
          {/* Header */}
          <Box sx={{ mb: 3 }}>
            <Typography variant="h5" fontWeight={700} gutterBottom>
              {career} Quiz
            </Typography>
            <Box sx={{ display: 'flex', alignItems: 'center', gap: 2, mb: 1 }}>
              <LinearProgress
                variant="determinate"
                value={progress}
                sx={{ flex: 1, height: 8, borderRadius: 4 }}
              />
              <Chip
                label={`${currentIndex + 1} / ${questions.length}`}
                size="small"
                color="primary"
              />
            </Box>
          </Box>

          {/* Question */}
          <Box sx={{ mb: 4 }}>
            <Typography variant="h6" sx={{ mb: 3 }}>
              {currentQuestion.question}
            </Typography>

            <RadioGroup
              value={answers[currentIndex] !== undefined ? String(answers[currentIndex]) : ''}
              onChange={(e) => handleAnswer(e.target.value)}
            >
              {currentQuestion.options.map((option, idx) => (
                <FormControlLabel
                  key={idx}
                  value={String(idx)}
                  control={<Radio />}
                  label={option}
                  sx={{
                    mb: 1,
                    border: '1px solid',
                    borderColor:
                      answers[currentIndex] === idx ? 'primary.main' : 'divider',
                    borderRadius: 2,
                    mx: 0,
                    px: 2,
                    py: 0.5,
                    bgcolor:
                      answers[currentIndex] === idx ? 'primary.50' : 'transparent',
                    '&:hover': { bgcolor: 'grey.100' },
                  }}
                />
              ))}
            </RadioGroup>
          </Box>

          {/* Navigation */}
          <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <Button
              startIcon={<ArrowBackIcon />}
              disabled={currentIndex === 0}
              onClick={() => setCurrentIndex((prev) => prev - 1)}
            >
              Previous
            </Button>

            {currentIndex < questions.length - 1 ? (
              <Button
                variant="contained"
                endIcon={<ArrowForwardIcon />}
                onClick={() => setCurrentIndex((prev) => prev + 1)}
              >
                Next
              </Button>
            ) : (
              <Button
                variant="contained"
                color="success"
                disabled={!allAnswered}
                onClick={handleSubmit}
              >
                Submit Quiz
              </Button>
            )}
          </Box>
        </Paper>
      </Container>
    </Box>
  );
}
