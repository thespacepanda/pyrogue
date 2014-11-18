"""
    tests.map_tests
    ~~~~~~~~~~~~~~~

    This module tests various properties of pyrogue.map.
"""

import pyrogue.map as m

def test_mark_cells_unvisited():
    """
    This test ensures that the map correctly marks all cells unvisited.
    """
    mock_map = m.Map(10, 10)
    mock_map.mark_cells_unvisited()

    for column in range(mock_map.width):
        for row in range(mock_map.height):
            assert mock_map[column, row].get_visited() is False

def test_random_mark_visited():
    """
    This test ensures we can randomly choose the current cell.
    """
    mock_map = m.Map(10, 10)
    mock_map.mark_cells_unvisited()
    mock_map.random_mark_visited()

    visited_count = 0
    for column in range(mock_map.width):
        for row in range(mock_map.height):
            if mock_map[column, row].get_visited():
                visited_count += 1

    assert visited_count == 1

def test_generator_instantiation():
    """
    This test ensures our generator can make a valid map.
    """
    gen = m.Generator(10, 10)
    mock_map = gen.generate()

    visited_count = 0
    for column in range(mock_map.width):
        for row in range(mock_map.height):
            if mock_map[column, row].get_visited():
                visited_count += 1
    assert visited_count == 100

def test_has_adjacent_in_direction():
    """
    This test ensures the adjacent cell code is functioning correctly.
    """
    mock_map = m.Map(10, 10)
    mock_map.mark_cells_unvisited()

    assert mock_map.has_adjacent_in_direction((1, 1), m.NORTH)
    assert mock_map.has_adjacent_in_direction((1, 1), m.WEST)
    assert mock_map.has_adjacent_in_direction(
        (mock_map.width - 2, mock_map.height - 2), m.SOUTH
    )
    assert mock_map.has_adjacent_in_direction(
        (mock_map.width - 2, mock_map.height - 2), m.EAST
    )

def test_no_adjacents_on_boundaries():
    """
    This test ensures there are no adjacent cells on the boundaries of
    the map.
    """
    mock_map = m.Map(10, 10)
    mock_map.mark_cells_unvisited()

    assert mock_map.has_adjacent_in_direction(
        (0, 0), m.NORTH
    ) is False
    assert mock_map.has_adjacent_in_direction(
        (0, 0), m.WEST
    ) is False
    assert mock_map.has_adjacent_in_direction(
        (mock_map.width - 1, mock_map.height - 1), m.SOUTH
    ) is False
    assert mock_map.has_adjacent_in_direction(
        (mock_map.width - 1, mock_map.height - 1), m.EAST
    ) is False

def test_no_adjacents_out_of_bounds():
    """
    This test ensures the function returns false when given an index
    that is out of bounds.
    """
    mock_map = m.Map(10, 10)
    mock_map.mark_cells_unvisited()

    assert mock_map.has_adjacent_in_direction(
        (-5, -5), m.NORTH
    ) is False

def test_adjacent_in_direction_visited():
    mock_map = m.Map(10, 10)
    mock_map.mark_cells_unvisited()

    mock_map.visited((1, 0))
    mock_map.visited((0, 1))
    mock_map.visited((1, 2))
    mock_map.visited((2, 1))

    assert mock_map.adjacent_in_direction_visited((1, 1), m.NORTH)
    assert mock_map.adjacent_in_direction_visited((1, 1), m.SOUTH)
    assert mock_map.adjacent_in_direction_visited((1, 1), m.EAST)
    assert mock_map.adjacent_in_direction_visited((1, 1), m.WEST)

def test_adjacent_in_direction_unvisited():
    mock_map = m.Map(10, 10)
    mock_map.mark_cells_unvisited()

    assert mock_map.adjacent_in_direction_visited(
        (1, 1), m.NORTH
    ) is False
    assert mock_map.adjacent_in_direction_visited(
        (1, 1), m.SOUTH
    ) is False
    assert mock_map.adjacent_in_direction_visited(
        (1, 1), m.EAST
    ) is False
    assert mock_map.adjacent_in_direction_visited(
        (1, 1), m.WEST
    ) is False

def test_direction_gen():
    gen = m.directions()
    seen_directions = []
    for direction in gen:
        assert (direction in seen_directions) is False
        seen_directions.append(direction)
    assert len(seen_directions) == 4

def test_get_random_visited():
    mock_map = m.Map(10, 10)
    mock_map.mark_cells_unvisited()

    mock_map.visited((1, 0))
    mock_map.visited((0, 1))
    mock_map.visited((1, 2))
    mock_map.visited((2, 1))

    current_cell = (2, 1)
    other_visited_cells = [(1, 0), (0, 1), (1, 2)]
    visited_cell = mock_map.random_visited_cell(current_cell)

    # check that the visited_cell is one of the others
    assert visited_cell in other_visited_cells

def test_corridor():
    mock_map = m.Map(10, 10)
    mock_map.mark_cells_unvisited()

    mock_map.corridor((0, 0), m.SOUTH)

    assert mock_map[0, 0].north_side
    assert not mock_map[0, 0].south_side
    assert mock_map[0, 0].east_side
    assert mock_map[0, 0].west_side

    assert not mock_map[0, 1].north_side
    assert mock_map[0, 1].south_side
    assert mock_map[0, 1].east_side
    assert mock_map[0, 1].west_side
