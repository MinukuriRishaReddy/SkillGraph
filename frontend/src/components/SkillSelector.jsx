import { useState } from 'react';
import Box from '@mui/material/Box';
import Chip from '@mui/material/Chip';
import Typography from '@mui/material/Typography';
import Paper from '@mui/material/Paper';
import TextField from '@mui/material/TextField';
import InputAdornment from '@mui/material/InputAdornment';
import SearchIcon from '@mui/icons-material/Search';

export default function SkillSelector({ title, skills, selectedIds, onToggle, color = 'primary' }) {
  const [search, setSearch] = useState('');

  const filtered = skills.filter((s) =>
    s.value.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <Paper variant="outlined" sx={{ p: 2.5, mb: 2 }}>
      <Box sx={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', mb: 1.5 }}>
        <Typography variant="subtitle1" fontWeight={600}>
          {title}
        </Typography>
        <Typography variant="caption" color="text.secondary">
          {selectedIds.filter((id) => skills.some((s) => s.id === id)).length} / {skills.length} selected
        </Typography>
      </Box>

      {skills.length > 8 && (
        <TextField
          size="small"
          placeholder={`Search ${title.toLowerCase()}...`}
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          fullWidth
          sx={{ mb: 1.5 }}
          InputProps={{
            startAdornment: (
              <InputAdornment position="start">
                <SearchIcon fontSize="small" />
              </InputAdornment>
            ),
          }}
        />
      )}

      <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 1 }}>
        {filtered.map((skill) => {
          const isSelected = selectedIds.includes(skill.id);
          return (
            <Chip
              key={skill.id}
              label={skill.value}
              color={isSelected ? color : 'default'}
              variant={isSelected ? 'filled' : 'outlined'}
              onClick={() => onToggle(skill.id)}
              sx={{ fontWeight: isSelected ? 600 : 400 }}
            />
          );
        })}
        {filtered.length === 0 && (
          <Typography variant="body2" color="text.secondary">
            No skills found
          </Typography>
        )}
      </Box>
    </Paper>
  );
}
