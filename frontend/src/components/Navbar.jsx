import { useState } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import Box from '@mui/material/Box';
import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';
import Drawer from '@mui/material/Drawer';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemText from '@mui/material/ListItemText';
import LogoutIcon from '@mui/icons-material/Logout';
import useMediaQuery from '@mui/material/useMediaQuery';

import logo from '../assets/icon.png'; // <-- your logo

export default function Navbar() {
  const navigate = useNavigate();
  const location = useLocation();
  const userId = localStorage.getItem('userId');
  const isMobile = useMediaQuery('(max-width:768px)');
  const [drawerOpen, setDrawerOpen] = useState(false);

  const handleLogout = () => {
    localStorage.removeItem('userId');
    localStorage.removeItem('userName');
    navigate('/login');
  };

  const navItems = userId
    ? [
        { label: 'Careers', path: '/careers' },
        { label: 'Skills', path: '/skills' },
        { label: 'Learning Path', path: '/learning-path' },
        { label: 'Skill Graph', path: '/skill-path' },
      ]
    : [];

  const isActive = (path) => location.pathname === path;

  const navContent = (
    <>
      {navItems.map((item) => (
        <Button
          key={item.path}
          onClick={() => {
            navigate(item.path);
            setDrawerOpen(false);
          }}
          sx={{
            color: '#fff',
            fontWeight: isActive(item.path) ? 700 : 400,
            borderBottom: isActive(item.path) ? '2px solid #fff' : 'none',
            borderRadius: 0,
            mx: 0.5,
          }}
        >
          {item.label}
        </Button>
      ))}

      {userId && (
        <Button
          onClick={handleLogout}
          startIcon={<LogoutIcon />}
          sx={{ color: '#fff', ml: 1 }}
        >
          Logout
        </Button>
      )}
    </>
  );

  return (
    <AppBar position="sticky" elevation={1}>
      <Toolbar>

        {/* Logo */}
        <Box
          component="img"
          src={logo}
          alt="SkilloGraph Logo"
          sx={{
            height: 28,
            mr: 1,
            cursor: 'pointer'
          }}
          onClick={() => navigate(userId ? '/careers' : '/login')}
        />

        {/* Title */}
        <Typography
          variant="h6"
          sx={{ flexGrow: 1, cursor: 'pointer', fontWeight: 700 }}
          onClick={() => navigate(userId ? '/careers' : '/login')}
        >
          SkilloGraph
        </Typography>

        {isMobile ? (
          <>
            <IconButton color="inherit" onClick={() => setDrawerOpen(true)}>
              <MenuIcon />
            </IconButton>

            <Drawer
              anchor="right"
              open={drawerOpen}
              onClose={() => setDrawerOpen(false)}
            >
              <Box sx={{ width: 220, pt: 2 }}>
                <List>
                  {navItems.map((item) => (
                    <ListItem key={item.path} disablePadding>
                      <ListItemButton
                        onClick={() => {
                          navigate(item.path);
                          setDrawerOpen(false);
                        }}
                        selected={isActive(item.path)}
                      >
                        <ListItemText primary={item.label} />
                      </ListItemButton>
                    </ListItem>
                  ))}

                  {userId && (
                    <ListItem disablePadding>
                      <ListItemButton onClick={handleLogout}>
                        <ListItemText primary="Logout" />
                      </ListItemButton>
                    </ListItem>
                  )}
                </List>
              </Box>
            </Drawer>
          </>
        ) : (
          <Box sx={{ display: 'flex', alignItems: 'center' }}>
            {navContent}
          </Box>
        )}
      </Toolbar>
    </AppBar>
  );
}