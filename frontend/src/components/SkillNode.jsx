import { memo } from 'react';
import { Handle, Position } from '@xyflow/react';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Tooltip from '@mui/material/Tooltip';
import LockIcon from '@mui/icons-material/Lock';
import PlayArrowIcon from '@mui/icons-material/PlayArrow';
import CheckCircleIcon from '@mui/icons-material/CheckCircle';

const STATUS_CONFIG = {
  locked: {
    bg: '#d32f2f',
    border: '#b71c1c',
    icon: LockIcon,
    label: 'Locked',
    cursor: 'not-allowed',
  },
  current: {
    bg: '#f9a825',
    border: '#f57f17',
    icon: PlayArrowIcon,
    label: 'Ready to learn',
    cursor: 'pointer',
  },
  completed: {
    bg: '#2e7d32',
    border: '#1b5e20',
    icon: CheckCircleIcon,
    label: 'Completed',
    cursor: 'default',
  },
};

function SkillNode({ data }) {
  const { label, status = 'locked', type, level } = data;
  const config = STATUS_CONFIG[status] || STATUS_CONFIG.locked;
  const Icon = config.icon;

  const tooltipContent = (
    <Box sx={{ p: 0.5 }}>
      <Typography variant="subtitle2" fontWeight={700}>
        {label}
      </Typography>
      {type && (
        <Typography variant="caption" display="block">
          Category: {type.replace('NEED_', '').replace(/([A-Z])/g, ' $1').trim()}
        </Typography>
      )}
      {level && (
        <Typography variant="caption" display="block">
          Level: {level}
        </Typography>
      )}
      <Typography variant="caption" display="block" sx={{ mt: 0.5, fontStyle: 'italic' }}>
        {config.label}
        {status === 'current' ? ' - Click to complete' : ''}
      </Typography>
    </Box>
  );

  return (
    <Tooltip title={tooltipContent} arrow placement="top">
      <Box
        sx={{
          background: `linear-gradient(135deg, ${config.bg} 0%, ${config.border} 100%)`,
          color: '#fff',
          borderRadius: '14px',
          padding: '14px 24px',
          minWidth: 150,
          textAlign: 'center',
          cursor: config.cursor,
          border: `3px solid ${config.border}`,
          boxShadow: status === 'current'
            ? `0 0 20px ${config.bg}80, 0 4px 12px rgba(0,0,0,0.15)`
            : '0 2px 8px rgba(0,0,0,0.12)',
          transition: 'all 0.3s ease',
          transform: status === 'current' ? 'scale(1.05)' : 'scale(1)',
          '&:hover': status === 'current'
            ? { transform: 'scale(1.1)', boxShadow: `0 0 28px ${config.bg}AA, 0 6px 16px rgba(0,0,0,0.2)` }
            : {},
        }}
      >
        <Handle type="target" position={Position.Left} style={{ background: config.border, width: 10, height: 10, border: '2px solid #fff' }} />

        <Box sx={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 1, mb: 0.5 }}>
          <Icon sx={{ fontSize: 20 }} />
        </Box>
        <Typography variant="body2" fontWeight={700} sx={{ lineHeight: 1.3 }}>
          {label}
        </Typography>
        <Typography variant="caption" sx={{ opacity: 0.85, display: 'block', mt: 0.3, fontSize: '0.65rem' }}>
          {config.label}
        </Typography>

        <Handle type="source" position={Position.Right} style={{ background: config.border, width: 10, height: 10, border: '2px solid #fff' }} />
      </Box>
    </Tooltip>
  );
}

export default memo(SkillNode);
