r"""
Often, one wants to construct new ML features from their current representation
in order to compress data or visualise trends in the dataset. In the archetypal
method for this dimensionality reduction, principal components analysis (PCA),
features are transformed into the latent space which best preserves the
variance of the original data. This module provides the Principal Covariates
Regression (PCovR), as introduced by [deJong1992]_, is a modification to PCA
that incorporates target information, such that the resulting embedding could
be tuned using a mixing parameter α to improve performance in regression tasks
(:math:`\alpha = 0` corresponding to linear regression and :math:`\alpha = 1`
corresponding to PCA).  [Helfrecht2020]_ introduced the non-linear version,
Kernel Principal Covariates Regression (KPCovR), where the mixing parameter α
now interpolates between kernel ridge regression (:math:`\alpha = 0`) and
kernel principal components analysis (KPCA, :math:`\alpha = 1`).

The module includes:

* :ref:`PCovR-api` the standard Principal Covariates Regression. Utilises a
  combination between a PCA-like and an LR-like loss, and therefore attempts to find
  a low-dimensional projection of the feature vectors that simultaneously minimises
  information loss and error in predicting the target properties using only the
  latent space vectors :math:`\mathbf{T}`.
* :ref:`KPCovR-api` the Kernel Principal Covariates Regression
  a kernel-based variation on the
  original PCovR method, proposed in [Helfrecht2020]_.
"""

from ._kernel_pcovr import KernelPCovR
from ._pcovr import (
    PCovR,
    pcovr_covariance,
    pcovr_kernel,
)

__all__ = ["pcovr_covariance", "pcovr_kernel", "PCovR", "KernelPCovR"]
