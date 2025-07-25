from sympy import SympifyError


class StmMatrixAnalysisError(Exception):
    """Base exception for matrix analysis failures"""
    def __init__(self, message: str, code: str = None):
        self.message = message
        self.code = code or "MATRIX_ANALYSIS_ERROR"
        super().__init__(message)


# --- Structure & Validation Errors ---

class StmInvalidMatrixError(StmMatrixAnalysisError):
    def __init__(self, detail: str):
        super().__init__(f"Invalid matrix: {detail}", code="INVALID_MATRIX")


class StmNotSquareMatrixError(StmMatrixAnalysisError):
    def __init__(self):
        super().__init__("Matrix must be square", code="NOT_SQUARE_MATRIX")


class StmNotSymmetricMatrixError(StmMatrixAnalysisError):
    def __init__(self):
        super().__init__("Matrix must be symmetric", code="NOT_SYMMETRIC_MATRIX")


class StmEmptyMatrixError(StmMatrixAnalysisError):
    def __init__(self):
        super().__init__("Matrix is empty", code="EMPTY_MATRIX")


class StmNonNumericMatrixError(StmMatrixAnalysisError):
    def __init__(self):
        super().__init__("Matrix contains non-numeric elements", code="NON_NUMERIC_MATRIX")


class StmContainsNaNOrInfError(StmMatrixAnalysisError):
    def __init__(self):
        super().__init__("Matrix contains NaN or infinite values", code="NAN_INF_ERROR")


class StmShapeMismatchError(StmMatrixAnalysisError):
    def __init__(self, detail: str):
        super().__init__(f"Shape mismatch: {detail}", code="SHAPE_MISMATCH")


class StmDimensionError(StmMatrixAnalysisError):
    def __init__(self, detail: str):
        super().__init__(f"Invalid matrix dimensions: {detail}", code="DIMENSION_ERROR")


# --- Algebraic & Computation Errors ---

class StmSingularMatrixError(StmMatrixAnalysisError):
    def __init__(self):
        super().__init__("Matrix is singular and not invertible", code="SINGULAR_MATRIX")


class StmNonPositiveDefiniteMatrixError(StmMatrixAnalysisError):
    def __init__(self):
        super().__init__("Matrix is not positive definite", code="NOT_POSITIVE_DEFINITE")


class StmDecompositionError(StmMatrixAnalysisError):
    def __init__(self, method: str):
        super().__init__(f"{method} decomposition failed", code="DECOMPOSITION_FAILED")


class StmEigenvalueComputationError(StmMatrixAnalysisError):
    def __init__(self):
        super().__init__("Failed to compute eigenvalues or eigenvectors", code="EIGENVALUE_ERROR")


class StmRankDeficientMatrixError(StmMatrixAnalysisError):
    def __init__(self):
        super().__init__("Matrix is rank-deficient", code="RANK_DEFICIENT")


class StmOrthogonalityError(StmMatrixAnalysisError):
    def __init__(self):
        super().__init__("Matrix is not orthogonal", code="NOT_ORTHOGONAL")


class StmNotDiagonalMatrixError(StmMatrixAnalysisError):
    def __init__(self):
        super().__init__("Matrix is not diagonal", code="NOT_DIAGONAL")


class StmNonInvertibleBlockError(StmMatrixAnalysisError):
    def __init__(self):
        super().__init__("One or more blocks in block matrix are not invertible", code="BLOCK_INVERT_ERROR")


# --- Numerical Stability & Precision ---

class StmNumericalPrecisionError(StmMatrixAnalysisError):
    def __init__(self, detail: str = "Result is numerically unstable"):
        super().__init__(detail, code="NUMERICAL_PRECISION_ERROR")


class StmConditionNumberError(StmMatrixAnalysisError):
    def __init__(self):
        super().__init__("Matrix is ill-conditioned (high condition number)", code="ILL_CONDITIONED")


class StmFloatingPointOverflowError(StmMatrixAnalysisError):
    def __init__(self):
        super().__init__("Floating point overflow occurred", code="FLOAT_OVERFLOW")


class StmFloatingPointUnderflowError(StmMatrixAnalysisError):
    def __init__(self):
        super().__init__("Floating point underflow occurred", code="FLOAT_UNDERFLOW")


class StmConvergenceError(StmMatrixAnalysisError):
    def __init__(self, method: str = "Iterative method"):
        super().__init__(f"{method} failed to converge", code="CONVERGENCE_ERROR")


# --- Context-Specific / Semantic Errors ---

class StmSparseMatrixRequiredError(StmMatrixAnalysisError):
    def __init__(self):
        super().__init__("Sparse matrix expected", code="SPARSE_MATRIX_REQUIRED")


class StmBinaryMatrixError(StmMatrixAnalysisError):
    def __init__(self):
        super().__init__("Matrix is expected to contain only 0s and 1s", code="BINARY_MATRIX_ERROR")


class StmMarkovMatrixError(StmMatrixAnalysisError):
    def __init__(self):
        super().__init__("Invalid Markov matrix: rows or columns do not sum to 1", code="MARKOV_MATRIX_ERROR")


class StmStochasticMatrixError(StmMatrixAnalysisError):
    def __init__(self):
        super().__init__("Matrix must be stochastic or doubly stochastic", code="STOCHASTIC_MATRIX_ERROR")


class StmTransitionMatrixError(StmMatrixAnalysisError):
    def __init__(self):
        super().__init__("Invalid transition matrix", code="TRANSITION_MATRIX_ERROR")


class StmGraphLaplacianError(StmMatrixAnalysisError):
    def __init__(self):
        super().__init__("Matrix is not a valid graph Laplacian", code="GRAPH_LAPLACIAN_ERROR")


class StmPSDMatrixError(StmMatrixAnalysisError):
    def __init__(self):
        super().__init__("Matrix is not positive semi-definite", code="NOT_PSD")
        

class StmMatrixCompatibilityError(StmMatrixAnalysisError):
    """Raised when matrices are incompatible for an operation"""
    def __init__(self, operation: str, shape_a, shape_b):
        super().__init__(
            f"Matrices are incompatible for {operation}: {shape_a} vs {shape_b}",
            code="MATRIX_COMPATIBILITY_ERROR"
        )