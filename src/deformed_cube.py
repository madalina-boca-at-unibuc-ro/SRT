from ursina import *

cube_side_length = 5
line_width = 0.05

# Default starting positions for when none are provided
default_starting_positions = [
    Vec3(0, 0, 0),
    Vec3(cube_side_length, 0, 0),
    Vec3(0, 0, cube_side_length),
    Vec3(cube_side_length, 0, cube_side_length),
    Vec3(0, cube_side_length, 0),
    Vec3(cube_side_length, cube_side_length, 0),
    Vec3(0, cube_side_length, cube_side_length),
    Vec3(cube_side_length, cube_side_length, cube_side_length),
]


class DeformedCube(Entity):
    def __init__(
        self,
        positions=None,
        sphere_color=color.white,
        line_color=color.gray,
    ):
        super().__init__()

        # Use provided positions or default ones
        if positions is None:
            positions = default_starting_positions

        assert len(positions) == 8, "You must provide exactly 8 vertex positions."

        # Create 8 spheres (vertices)
        self.vertices = []
        for pos in positions:
            s = Entity(model="sphere", color=sphere_color, position=pos, scale=0.1)
            self.vertices.append(s)

        # Define cube edges (pairs of vertex indices)
        self.edges = [
            (0, 1),
            (1, 3),
            (3, 2),
            (2, 0),  # Bottom face
            (4, 5),
            (5, 7),
            (7, 6),
            (6, 4),  # Top face
            (0, 4),
            (1, 5),
            (2, 6),
            (3, 7),  # Vertical edges
        ]

        # Create connecting lines
        self.lines = []
        for start_idx, end_idx in self.edges:
            start = self.vertices[start_idx]
            end = self.vertices[end_idx]
            midpoint = (start.position + end.position) / 2
            length = distance(start.position, end.position)
            line = Entity(
                model="cube",
                position=midpoint,
                scale=(line_width, line_width, length),
                color=line_color,
            )
            line.look_at(end.position)
            self.lines.append(line)

    def set_vertex_position(self, new_positions=None):
        """Update position of vertex at index and refresh lines"""
        if new_positions is None:
            return
        else:
            for vertex, new_position in zip(self.vertices, new_positions):
                vertex.position = new_position
            return

    def update_lines(self):
        """Refresh line positions and orientations"""
        for i, (start_idx, end_idx) in enumerate(self.edges):
            start = self.vertices[start_idx]
            end = self.vertices[end_idx]
            midpoint = (start.position + end.position) / 2
            direction = end.position - start.position
            length = direction.length()

            line = self.lines[i]
            line.position = midpoint
            line.scale = (line_width, line_width, length)
            line.look_at(end.position)
        return

    def update(self, new_positions=None):
        if new_positions is not None:
            self.set_vertex_position(new_positions)
            self.update_lines()
            return
        else:
            return

    def cleanup(self):
        """Clean up all child entities"""
        if hasattr(self, "vertices"):
            for vertex in self.vertices:
                if vertex:
                    destroy(vertex)
            self.vertices.clear()

        if hasattr(self, "lines"):
            for line in self.lines:
                if line:
                    destroy(line)
            self.lines.clear()
