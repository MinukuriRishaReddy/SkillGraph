import Card from '@mui/material/Card';
import CardActionArea from '@mui/material/CardActionArea';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';
import WorkIcon from '@mui/icons-material/Work';
import Box from '@mui/material/Box';
import CheckCircleIcon from '@mui/icons-material/CheckCircle';

export default function CareerCard({ career, selected, onClick }) {
  return (
    <Card
      sx={{
        border: selected ? '2px solid' : '1px solid',
        borderColor: selected ? 'primary.main' : 'divider',
        bgcolor: selected ? 'primary.50' : 'background.paper',
        transition: 'all 0.2s',
        '&:hover': { borderColor: 'primary.main', transform: 'translateY(-2px)', boxShadow: 3 },
      }}
    >
      <CardActionArea onClick={onClick} sx={{ p: 1 }}>
        <CardContent>
          <Box sx={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
            <Box sx={{ display: 'flex', alignItems: 'center', gap: 1.5 }}>
              <WorkIcon color={selected ? 'primary' : 'action'} />
              <Typography variant="h6" fontWeight={600}>
                {career.creTitle}
              </Typography>
            </Box>
            {selected && <CheckCircleIcon color="primary" />}
          </Box>
        </CardContent>
      </CardActionArea>
    </Card>
  );
}
