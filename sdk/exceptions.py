class MatrixAnalysisError(Exception):
    """Base exception for matrix analysis failures"""
    def __init__(self, message: str, code: str = None):
        self.message = message
        self.code = code or "MATRIX_ANALYSIS_ERROR"
        super().__init__(message)

class InvalidMatrixError(MatrixAnalysisError):
    """Raised when matrix structure is invalid"""
    def __init__(self, detail: str):
        super().__init__(
            f"Invalid matrix: {detail}",
            code="INVALID_MATRIX"
        )