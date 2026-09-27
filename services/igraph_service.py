import os
import logging

import igraph

logger = logging.getLogger(__name__)

# Ensure static directory exists
STATIC_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'static')
os.makedirs(STATIC_DIR, exist_ok=True)


def visualize_learning_path_v1(set_course, index):
    """Visualize a v1 learning path as a directed circular graph."""
    try:
        i_graph = igraph.Graph(directed=True)
        n = len(set_course)
        i_graph.add_vertices(n)
        i_graph.vs["name"] = set_course
        edges = [(i, i + 1) for i in range(n - 1)]
        i_graph.add_edges(edges)
        layout = i_graph.layout_circle()
        visual_style = {
            "vertex_size": 100,
            "layout": layout,
            "vertex_color": "cyan",
            "vertex_label": i_graph.vs["name"],
            "edge_width": 5,
            "bbox": (900, 900),
            "margin": 100
        }
        file_name = os.path.join(STATIC_DIR, f"learning-path-{index}.png")
        igraph.plot(i_graph, file_name, **visual_style)
        logger.info(f"Generated visualization: {file_name}")
    except Exception as e:
        logger.error(f"Failed to generate v1 visualization: {e}")
        raise


def visualize_learning_path_v2(path_final, index):
    """Visualize a v2 learning path as a directed tree graph."""
    try:
        i_graph = igraph.Graph(directed=True)
        size_graph = sum(len(path) for path in path_final)

        if size_graph == 0:
            logger.warning(f"Empty path for visualization {index}")
            return

        i_graph.add_vertices(size_graph)
        edges = []
        vertices = []
        counter = 0

        for path in path_final:
            vertices.extend(path)
            if len(path) > 1:
                for i in range(len(path) - 1):
                    edges.append((counter + i, counter + i + 1))
            counter += len(path)

        i_graph.vs["id"] = vertices
        i_graph.add_edges(edges)

        max_size = max((len(p) for p in path_final), default=1)
        layout = i_graph.layout_reingold_tilford()

        width = max(len(path_final) * 50 + 100, 300)
        height = max(max_size * 70 + 100, 200)

        visual_style = {
            "vertex_size": 50,
            "layout": layout,
            "vertex_color": "orange",
            "vertex_label": i_graph.vs["id"],
            "edge_width": 2,
            "bbox": (width, height),
            "margin": 50
        }
        file_name = os.path.join(STATIC_DIR, f"learning-path-{index}.png")
        igraph.plot(i_graph, file_name, **visual_style)
        logger.info(f"Generated visualization: {file_name}")
    except Exception as e:
        logger.error(f"Failed to generate v2 visualization: {e}")
        raise
