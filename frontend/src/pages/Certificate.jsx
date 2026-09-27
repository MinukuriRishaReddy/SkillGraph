import { useEffect, useRef, useState, useCallback } from 'react';
import { useSearchParams, useNavigate } from 'react-router-dom';
import Box from '@mui/material/Box';
import Container from '@mui/material/Container';
import Paper from '@mui/material/Paper';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import CircularProgress from '@mui/material/CircularProgress';
import DownloadIcon from '@mui/icons-material/Download';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import { getUserInfo } from '../api/api';

export default function Certificate() {
  const [searchParams] = useSearchParams();
  const navigate = useNavigate();
  const canvasRef = useRef(null);
  const career = searchParams.get('career') || '';
  const [userName, setUserName] = useState('');
  const [loading, setLoading] = useState(true);

  // Fetch user name
  useEffect(() => {
    const userId = localStorage.getItem('userId');
    if (!userId) {
      setUserName(localStorage.getItem('userName') || 'Student');
      setLoading(false);
      return;
    }
    getUserInfo(userId)
      .then((res) => {
        const name = res.data?.name || res.data?.user?.name || localStorage.getItem('userName') || 'Student';
        setUserName(name);
      })
      .catch(() => {
        setUserName(localStorage.getItem('userName') || 'Student');
      })
      .finally(() => setLoading(false));
  }, []);

  const drawCertificate = useCallback(() => {
    const canvas = canvasRef.current;
    if (!canvas || !userName) return;

    const ctx = canvas.getContext('2d');
    const W = 1120;
    const H = 800;
    canvas.width = W;
    canvas.height = H;

    // Background
    ctx.fillStyle = '#FFFFFF';
    ctx.fillRect(0, 0, W, H);

    // Outer border - dark blue
    ctx.strokeStyle = '#1a237e';
    ctx.lineWidth = 8;
    ctx.strokeRect(20, 20, W - 40, H - 40);

    // Inner border - gold
    ctx.strokeStyle = '#c9a84c';
    ctx.lineWidth = 3;
    ctx.strokeRect(35, 35, W - 70, H - 70);

    // Decorative corner ornaments
    const cornerSize = 40;
    const corners = [
      [45, 45],
      [W - 45 - cornerSize, 45],
      [45, H - 45 - cornerSize],
      [W - 45 - cornerSize, H - 45 - cornerSize],
    ];
    ctx.fillStyle = '#c9a84c';
    corners.forEach(([x, y]) => {
      ctx.beginPath();
      ctx.moveTo(x + cornerSize / 2, y);
      ctx.lineTo(x + cornerSize, y + cornerSize / 2);
      ctx.lineTo(x + cornerSize / 2, y + cornerSize);
      ctx.lineTo(x, y + cornerSize / 2);
      ctx.closePath();
      ctx.fill();
    });

    // Top decorative line
    ctx.beginPath();
    ctx.strokeStyle = '#c9a84c';
    ctx.lineWidth = 2;
    ctx.moveTo(100, 120);
    ctx.lineTo(W - 100, 120);
    ctx.stroke();

    // "Certificate of Completion" header
    ctx.fillStyle = '#1a237e';
    ctx.font = '600 22px Georgia, serif';
    ctx.textAlign = 'center';
    ctx.fillText('CERTIFICATE', W / 2, 170);

    ctx.fillStyle = '#444';
    ctx.font = '18px Georgia, serif';
    ctx.fillText('OF COMPLETION', W / 2, 200);

    // Decorative line below header
    ctx.beginPath();
    ctx.strokeStyle = '#c9a84c';
    ctx.lineWidth = 1.5;
    ctx.moveTo(W / 2 - 120, 220);
    ctx.lineTo(W / 2 + 120, 220);
    ctx.stroke();

    // "This is to certify that"
    ctx.fillStyle = '#666';
    ctx.font = '18px Georgia, serif';
    ctx.fillText('This is to certify that', W / 2, 280);

    // User name
    ctx.fillStyle = '#1a237e';
    ctx.font = 'bold 42px Georgia, serif';
    ctx.fillText(userName, W / 2, 340);

    // Underline below name
    const nameWidth = ctx.measureText(userName).width;
    ctx.beginPath();
    ctx.strokeStyle = '#c9a84c';
    ctx.lineWidth = 2;
    ctx.moveTo(W / 2 - nameWidth / 2 - 20, 355);
    ctx.lineTo(W / 2 + nameWidth / 2 + 20, 355);
    ctx.stroke();

    // "has successfully completed"
    ctx.fillStyle = '#666';
    ctx.font = '18px Georgia, serif';
    ctx.fillText('has successfully completed the learning path and assessment for', W / 2, 410);

    // Career name
    ctx.fillStyle = '#1a237e';
    ctx.font = 'bold 32px Georgia, serif';
    ctx.fillText(career, W / 2, 465);

    // Date
    const today = new Date().toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
    });
    ctx.fillStyle = '#666';
    ctx.font = '16px Georgia, serif';
    ctx.fillText(`Awarded on ${today}`, W / 2, 530);

    // Bottom decorative line
    ctx.beginPath();
    ctx.strokeStyle = '#c9a84c';
    ctx.lineWidth = 2;
    ctx.moveTo(100, 580);
    ctx.lineTo(W - 100, 580);
    ctx.stroke();

    // SkillGraph branding
    ctx.fillStyle = '#1a237e';
    ctx.font = 'bold 24px Georgia, serif';
    ctx.fillText('SkillGraph', W / 2, 640);

    ctx.fillStyle = '#888';
    ctx.font = '14px Georgia, serif';
    ctx.fillText('Learning Path Recommendation System', W / 2, 665);

    // Signature line
    ctx.beginPath();
    ctx.strokeStyle = '#333';
    ctx.lineWidth = 1;
    ctx.moveTo(W / 2 - 100, 720);
    ctx.lineTo(W / 2 + 100, 720);
    ctx.stroke();

    ctx.fillStyle = '#666';
    ctx.font = '14px Georgia, serif';
    ctx.fillText('Verified Certificate', W / 2, 740);
  }, [userName, career]);

  // Draw when ready
  useEffect(() => {
    if (!loading && userName) {
      drawCertificate();
    }
  }, [loading, userName, drawCertificate]);

  const handleDownload = () => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const link = document.createElement('a');
    link.download = `${career.replace(/\s+/g, '_')}_Certificate.png`;
    link.href = canvas.toDataURL('image/png');
    link.click();
  };

  if (!career) {
    return (
      <Box sx={{ minHeight: 'calc(100vh - 64px)', bgcolor: 'grey.50', py: 6 }}>
        <Container maxWidth="sm">
          <Paper sx={{ p: 4, textAlign: 'center' }}>
            <Typography variant="h5" gutterBottom>
              Certificate Not Available
            </Typography>
            <Typography color="text.secondary" sx={{ mb: 3 }}>
              No career specified. Please complete a quiz first.
            </Typography>
            <Button variant="contained" onClick={() => navigate('/skill-path')}>
              Go to Learning Path
            </Button>
          </Paper>
        </Container>
      </Box>
    );
  }

  return (
    <Box sx={{ minHeight: 'calc(100vh - 64px)', bgcolor: 'grey.50', py: 6 }}>
      <Container maxWidth="lg">
        <Paper sx={{ p: 4 }}>
          <Typography variant="h4" fontWeight={700} textAlign="center" gutterBottom>
            Your Certificate
          </Typography>
          <Typography variant="body1" color="text.secondary" textAlign="center" sx={{ mb: 4 }}>
            Congratulations on completing the {career} learning path!
          </Typography>

          {loading ? (
            <Box sx={{ display: 'flex', justifyContent: 'center', py: 8 }}>
              <CircularProgress />
            </Box>
          ) : (
            <>
              <Box
                sx={{
                  display: 'flex',
                  justifyContent: 'center',
                  mb: 4,
                  overflow: 'auto',
                }}
              >
                <canvas
                  ref={canvasRef}
                  style={{
                    maxWidth: '100%',
                    height: 'auto',
                    border: '1px solid #e0e0e0',
                    borderRadius: 8,
                    boxShadow: '0 4px 20px rgba(0,0,0,0.1)',
                  }}
                />
              </Box>

              <Box sx={{ display: 'flex', gap: 2, justifyContent: 'center' }}>
                <Button
                  variant="contained"
                  size="large"
                  startIcon={<DownloadIcon />}
                  onClick={handleDownload}
                >
                  Download Certificate
                </Button>
                <Button
                  variant="outlined"
                  size="large"
                  startIcon={<ArrowBackIcon />}
                  onClick={() => navigate('/skill-path')}
                >
                  Back to Learning Path
                </Button>
              </Box>
            </>
          )}
        </Paper>
      </Container>
    </Box>
  );
}
