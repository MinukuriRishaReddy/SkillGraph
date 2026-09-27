import { useState, useCallback, useMemo, useEffect, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import {
  ReactFlow,
  Background,
  Controls,
  MiniMap,
  useNodesState,
  useEdgesState,
} from '@xyflow/react';
import '@xyflow/react/dist/style.css';
import confetti from 'canvas-confetti';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Alert from '@mui/material/Alert';
import Button from '@mui/material/Button';
import Fade from '@mui/material/Fade';
import EmojiEventsIcon from '@mui/icons-material/EmojiEvents';
import QuizIcon from '@mui/icons-material/Quiz';
import SkillNode from './SkillNode';

const nodeTypes = { skillNode: SkillNode };

/**
 * Find root nodes (nodes with no incoming edges).
 */
function findRoots(skills, relations) {
  const targets = new Set(relations.map((r) => r.target));
  return skills.filter((s) => !targets.has(s.id)).map((s) => s.id);
}

/**
 * Topological sort via BFS (Kahn's algorithm) for left-to-right layout.
 */
function topoSort(skills, relations) {
  const adj = {};
  const inDegree = {};
  const skillMap = {};

  skills.forEach((s) => {
    adj[s.id] = [];
    inDegree[s.id] = 0;
    skillMap[s.id] = s;
  });

  relations.forEach((r) => {
    if (adj[r.source]) {
      adj[r.source].push(r.target);
      inDegree[r.target] = (inDegree[r.target] || 0) + 1;
    }
  });

  const queue = Object.keys(inDegree).filter((id) => inDegree[id] === 0);
  const layers = [];

  while (queue.length > 0) {
    const nextQueue = [];
    const layer = [...queue];
    layers.push(layer);

    for (const nodeId of queue) {
      for (const neighbor of adj[nodeId] || []) {
        inDegree[neighbor]--;
        if (inDegree[neighbor] === 0) {
          nextQueue.push(neighbor);
        }
      }
    }
    queue.length = 0;
    queue.push(...nextQueue);
  }

  return layers;
}

/**
 * Determine initial statuses respecting user's existing skills AND dependency order.
 * A user skill is only marked 'completed' if all its prerequisites are also completed.
 * This walks the graph layer by layer (topological order) so dependencies are honoured.
 */
function getInitialStatuses(skills, relations, userSkillIds = new Set()) {
  const layers = topoSort(skills, relations);

  // Build prereq map: skillId -> [prerequisite skill IDs]
  const prereqMap = {};
  skills.forEach((s) => { prereqMap[s.id] = []; });
  relations.forEach((r) => {
    if (prereqMap[r.target]) prereqMap[r.target].push(r.source);
  });

  const statuses = {};
  skills.forEach((s) => { statuses[s.id] = 'locked'; });

  // Walk layer by layer — earlier layers are prerequisites for later ones
  for (const layer of layers) {
    for (const skillId of layer) {
      const prereqs = prereqMap[skillId] || [];
      const allPrereqsDone = prereqs.every((pid) => statuses[pid] === 'completed');

      if (userSkillIds.has(skillId) && allPrereqsDone) {
        // User has this skill and all prereqs are done → completed
        statuses[skillId] = 'completed';
      } else if (allPrereqsDone) {
        // Prereqs done but user doesn't have this skill → current (clickable)
        statuses[skillId] = 'current';
      }
      // Otherwise stays 'locked'
    }
  }

  return statuses;
}

/**
 * Build React Flow nodes and edges from skill data.
 */
function buildGraph(skills, relations, statuses) {
  const layers = topoSort(skills, relations);
  const skillMap = {};
  skills.forEach((s) => { skillMap[s.id] = s; });

  const X_SPACING = 280;
  const Y_SPACING = 120;

  const nodes = [];
  layers.forEach((layer, col) => {
    const yOffset = -(layer.length - 1) * Y_SPACING / 2;
    layer.forEach((skillId, row) => {
      const skill = skillMap[skillId];
      if (!skill) return;
      nodes.push({
        id: skillId,
        type: 'skillNode',
        position: { x: col * X_SPACING, y: yOffset + row * Y_SPACING },
        data: {
          label: skill.name,
          status: statuses[skillId] || 'locked',
          type: skill.type,
          level: skill.level,
        },
      });
    });
  });

  const edges = relations.map((r) => ({
    id: `e-${r.source}-${r.target}`,
    source: r.source,
    target: r.target,
    type: 'smoothstep',
    animated: statuses[r.source] === 'completed' && statuses[r.target] === 'current',
    style: {
      stroke:
        statuses[r.source] === 'completed'
          ? '#2e7d32'
          : statuses[r.source] === 'current'
            ? '#f9a825'
            : '#9e9e9e',
      strokeWidth: 2.5,
    },
  }));

  return { nodes, edges };
}

export default function SkillGraphView({ skills, relations, career, userSkillIds = new Set() }) {
  const navigate = useNavigate();
  const [statuses, setStatuses] = useState(() => getInitialStatuses(skills, relations, userSkillIds));
  const [completed, setCompleted] = useState(false);

  // Build adjacency for fast prerequisite lookup
  const prereqMap = useMemo(() => {
    const map = {};
    skills.forEach((s) => { map[s.id] = []; });
    relations.forEach((r) => {
      if (map[r.target]) map[r.target].push(r.source);
    });
    return map;
  }, [skills, relations]);

  // Build graph from current statuses
  const { nodes: graphNodes, edges: graphEdges } = useMemo(
    () => buildGraph(skills, relations, statuses),
    [skills, relations, statuses]
  );

  const [nodes, setNodes, onNodesChange] = useNodesState(graphNodes);
  const [edges, setEdges, onEdgesChange] = useEdgesState(graphEdges);

  // Sync nodes/edges when statuses change
  useEffect(() => {
    const { nodes: newNodes, edges: newEdges } = buildGraph(skills, relations, statuses);
    setNodes(newNodes);
    setEdges(newEdges);
  }, [statuses, skills, relations, setNodes, setEdges]);

  // Fire confetti celebration
  const fireConfetti = useCallback(() => {
    const duration = 3000;
    const end = Date.now() + duration;

    const frame = () => {
      // Left side burst
      confetti({
        particleCount: 3,
        angle: 60,
        spread: 55,
        origin: { x: 0, y: 0.6 },
        colors: ['#2e7d32', '#f9a825', '#1976d2', '#9c27b0', '#ff9800'],
      });
      // Right side burst
      confetti({
        particleCount: 3,
        angle: 120,
        spread: 55,
        origin: { x: 1, y: 0.6 },
        colors: ['#2e7d32', '#f9a825', '#1976d2', '#9c27b0', '#ff9800'],
      });

      if (Date.now() < end) {
        requestAnimationFrame(frame);
      }
    };

    // Initial big burst from center
    confetti({
      particleCount: 100,
      spread: 70,
      origin: { x: 0.5, y: 0.5 },
      colors: ['#2e7d32', '#f9a825', '#1976d2', '#9c27b0', '#ff9800'],
    });

    // Continuous side bursts
    frame();
  }, []);

  // Check completion
  useEffect(() => {
    const allCompleted = skills.every((s) => statuses[s.id] === 'completed');
    if (allCompleted && !completed) {
      fireConfetti();
    }
    setCompleted(allCompleted);
  }, [statuses, skills, completed, fireConfetti]);

  const onNodeClick = useCallback(
    (_event, node) => {
      const currentStatus = statuses[node.id];
      if (currentStatus !== 'current') return;

      setStatuses((prev) => {
        const next = { ...prev, [node.id]: 'completed' };

        // Find children (skills that depend on this node)
        const children = relations
          .filter((r) => r.source === node.id)
          .map((r) => r.target);

        // Unlock children whose ALL prerequisites are now completed
        children.forEach((childId) => {
          const prereqs = prereqMap[childId] || [];
          const allPrereqsDone = prereqs.every((pid) => next[pid] === 'completed');
          if (allPrereqsDone && next[childId] === 'locked') {
            next[childId] = 'current';
          }
        });

        return next;
      });
    },
    [statuses, relations, prereqMap]
  );

  const onInit = useCallback((instance) => {
    setTimeout(() => instance.fitView({ padding: 0.3 }), 100);
  }, []);

  if (!skills || skills.length === 0) return null;

  const completedCount = Object.values(statuses).filter((s) => s === 'completed').length;

  return (
    <Box>
      {/* Progress bar */}
      <Box sx={{ mb: 2, display: 'flex', alignItems: 'center', gap: 2 }}>
        <Box sx={{ flex: 1, bgcolor: 'grey.200', borderRadius: 2, height: 10, overflow: 'hidden' }}>
          <Box
            sx={{
              width: `${(completedCount / skills.length) * 100}%`,
              height: '100%',
              bgcolor: 'success.main',
              borderRadius: 2,
              transition: 'width 0.5s ease',
            }}
          />
        </Box>
        <Typography variant="body2" fontWeight={600} color="text.secondary" sx={{ minWidth: 80 }}>
          {completedCount} / {skills.length}
        </Typography>
      </Box>

      {/* Completion message */}
      <Fade in={completed}>
        <Box>
          {completed && (
            <Alert
              severity="success"
              icon={<EmojiEventsIcon />}
              sx={{ mb: 2, fontWeight: 600 }}
              action={
                <Button
                  color="inherit"
                  size="small"
                  startIcon={<QuizIcon />}
                  onClick={() => navigate(`/quiz?career=${encodeURIComponent(career)}`)}
                  sx={{ fontWeight: 600 }}
                >
                  Take Quiz
                </Button>
              }
            >
              Congratulations! You completed the {career} learning path. Take the quiz to earn your certificate!
            </Alert>
          )}
        </Box>
      </Fade>

      {/* Legend */}
      <Box sx={{ display: 'flex', gap: 3, mb: 2, flexWrap: 'wrap' }}>
        {[
          { color: '#d32f2f', label: 'Locked' },
          { color: '#f9a825', label: 'Current (click to complete)' },
          { color: '#2e7d32', label: 'Completed' },
        ].map((item) => (
          <Box key={item.label} sx={{ display: 'flex', alignItems: 'center', gap: 0.8 }}>
            <Box sx={{ width: 14, height: 14, borderRadius: '50%', bgcolor: item.color }} />
            <Typography variant="caption" color="text.secondary">{item.label}</Typography>
          </Box>
        ))}
      </Box>

      {/* Graph */}
      <Box
        sx={{
          width: '100%',
          height: 520,
          border: '1px solid',
          borderColor: 'divider',
          borderRadius: 2,
          overflow: 'hidden',
          bgcolor: '#fafbfc',
        }}
      >
        <ReactFlow
          nodes={nodes}
          edges={edges}
          onNodesChange={onNodesChange}
          onEdgesChange={onEdgesChange}
          onNodeClick={onNodeClick}
          onInit={onInit}
          nodeTypes={nodeTypes}
          fitView
          attributionPosition="bottom-left"
          minZoom={0.3}
          maxZoom={2}
        >
          <Background color="#e0e0e0" gap={24} size={1} />
          <Controls showInteractive={false} />
          <MiniMap
            nodeStrokeWidth={3}
            pannable
            zoomable
            style={{ height: 100, width: 160 }}
            nodeColor={(node) => {
              const s = node.data?.status;
              if (s === 'completed') return '#2e7d32';
              if (s === 'current') return '#f9a825';
              return '#d32f2f';
            }}
          />
        </ReactFlow>
      </Box>
    </Box>
  );
}
