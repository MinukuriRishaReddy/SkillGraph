import { useMemo, useCallback } from 'react';
import {
  ReactFlow,
  Background,
  Controls,
  MiniMap,
  useNodesState,
  useEdgesState,
} from '@xyflow/react';
import '@xyflow/react/dist/style.css';
import Box from '@mui/material/Box';

const NODE_COLORS = {
  course: '#1976d2',
  skill: '#2e7d32',
  start: '#ed6c02',
  end: '#9c27b0',
};

function buildGraph(courses) {
  const nodes = [];
  const edges = [];

  if (!courses || courses.length === 0) return { nodes, edges };

  // Start node
  nodes.push({
    id: 'start',
    data: { label: 'Start' },
    position: { x: 0, y: 0 },
    style: {
      background: NODE_COLORS.start,
      color: '#fff',
      borderRadius: '50%',
      width: 80,
      height: 80,
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      fontWeight: 700,
      fontSize: 14,
      border: 'none',
    },
  });

  const spacing = 250;

  courses.forEach((course, i) => {
    const nodeId = `course-${course.id || i}`;
    nodes.push({
      id: nodeId,
      data: {
        label: course.name || `Course ${i + 1}`,
      },
      position: { x: (i + 1) * spacing, y: Math.sin(i * 0.8) * 80 },
      style: {
        background: NODE_COLORS.course,
        color: '#fff',
        borderRadius: 12,
        padding: '12px 20px',
        fontWeight: 600,
        fontSize: 13,
        border: 'none',
        minWidth: 140,
        textAlign: 'center',
      },
    });

    // Connect to previous node
    const sourceId = i === 0 ? 'start' : `course-${courses[i - 1].id || (i - 1)}`;
    edges.push({
      id: `e-${sourceId}-${nodeId}`,
      source: sourceId,
      target: nodeId,
      animated: true,
      style: { stroke: '#1976d2', strokeWidth: 2 },
    });

    // Add provided skills as sub-nodes
    if (course.provides && course.provides.length > 0) {
      course.provides.forEach((skill, j) => {
        const skillId = `skill-${course.id || i}-${j}`;
        nodes.push({
          id: skillId,
          data: { label: skill.name || skill.value || skill },
          position: {
            x: (i + 1) * spacing + (j - (course.provides.length - 1) / 2) * 120,
            y: Math.sin(i * 0.8) * 80 + 120,
          },
          style: {
            background: NODE_COLORS.skill,
            color: '#fff',
            borderRadius: 8,
            padding: '6px 14px',
            fontSize: 11,
            border: 'none',
          },
        });
        edges.push({
          id: `e-${nodeId}-${skillId}`,
          source: nodeId,
          target: skillId,
          style: { stroke: '#2e7d32', strokeWidth: 1, strokeDasharray: '5,5' },
        });
      });
    }
  });

  // End node
  const lastCourse = courses[courses.length - 1];
  const endId = 'end';
  nodes.push({
    id: endId,
    data: { label: 'Goal' },
    position: { x: (courses.length + 1) * spacing, y: 0 },
    style: {
      background: NODE_COLORS.end,
      color: '#fff',
      borderRadius: '50%',
      width: 80,
      height: 80,
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      fontWeight: 700,
      fontSize: 14,
      border: 'none',
    },
  });
  edges.push({
    id: `e-last-end`,
    source: `course-${lastCourse.id || (courses.length - 1)}`,
    target: endId,
    animated: true,
    style: { stroke: '#9c27b0', strokeWidth: 2 },
  });

  return { nodes, edges };
}

export default function GraphView({ courses }) {
  const { nodes: initialNodes, edges: initialEdges } = useMemo(
    () => buildGraph(courses),
    [courses]
  );

  const [nodes, , onNodesChange] = useNodesState(initialNodes);
  const [edges, , onEdgesChange] = useEdgesState(initialEdges);

  const onInit = useCallback((instance) => {
    setTimeout(() => instance.fitView({ padding: 0.2 }), 100);
  }, []);

  if (!courses || courses.length === 0) {
    return null;
  }

  return (
    <Box sx={{ width: '100%', height: 500, border: '1px solid', borderColor: 'divider', borderRadius: 2, overflow: 'hidden' }}>
      <ReactFlow
        nodes={nodes}
        edges={edges}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        onInit={onInit}
        fitView
        attributionPosition="bottom-left"
      >
        <Background color="#e0e0e0" gap={20} />
        <Controls />
        <MiniMap
          nodeStrokeWidth={3}
          pannable
          zoomable
          style={{ height: 100, width: 160 }}
        />
      </ReactFlow>
    </Box>
  );
}
