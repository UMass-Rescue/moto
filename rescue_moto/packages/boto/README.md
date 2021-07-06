## Removing the `boto` Dependency

In order to rid `rescue_moto` of a direct dependency on the long-deprecated `boto` 
package, a subset of the `boto` code has been vendored here.

This directory contains only the `boto` files required for `rescue_moto` to run, 
which is a very small subset of the original package's contents.  Furthermore, 
the `boto` models collected here have been stripped of all superfluous 
methods/attributes not used by `rescue_moto`.  (Any copyright headers on the 
original files have been left intact.)

## Next Steps

Currently, a small number of `rescue_moto` models inherit from these `boto` classes.
With some additional work, the inheritance can be dropped in favor of simply
adding the required methods/properties from these `boto` models to their 
respective `rescue_moto` subclasses, which would allow for these files/directories 
to be removed entirely.