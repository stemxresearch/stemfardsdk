from stemfardsdk.matrix_analysis import matrix_analysis


def test_basic_analysis():
    result = matrix_analysis([[1, 2], [3, 4]])
    assert result.shape == [2, 2]
    assert result.is_square is True
    assert result.determinant == -2.0
