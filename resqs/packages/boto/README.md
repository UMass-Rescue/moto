## Removing the `boto` Dependency

In order to rid `resqs` of a direct dependency on the long-deprecated `boto` 
package, a subset of the `boto` code has been vendored here.

This directory contains only the `boto` files required for `resqs` to run, 
which is a very small subset of the original package's contents.  Furthermore, 
the `boto` models collected here have been stripped of all superfluous 
methods/attributes not used by `resqs`.  (Any copyright headers on the 
original files have been left intact.)

## Next Steps

Currently, a small number of `resqs` models inherit from these `boto` classes.
With some additional work, the inheritance can be dropped in favor of simply
adding the required methods/properties from these `boto` models to their 
respective `resqs` subclasses, which would allow for these files/directories 
to be removed entirely.