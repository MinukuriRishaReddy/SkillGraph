import React from 'react';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';

const Footer = () => {
  return (
    <Box
      component="footer"
      sx={{
        py: 3,
        px: 2,
        mt: 'auto',
        backgroundColor: '#f5f5f5',
        borderTop: '1px solid #ddd',
        textAlign: 'center',
      }}
    >
      <Container maxWidth="lg">
        <Typography variant="subtitle1" fontWeight="bold" color="text.primary" gutterBottom>
          Your Personalized Learning Path Navigator
        </Typography>
        <Typography variant="body2" color="text.secondary">
          © 2026 SkillGraph. All Rights Reserved.
        </Typography>
      </Container>
    </Box>
  );
};

export default Footer;
