#!/usr/bin/env python3
from itertools import product

# Capability-lattice check: reads need scope; mutations need scope plus write authority.
for authenticated, tenant_scoped, mutating, write_scope in product((False, True), repeat=4):
    admitted = authenticated and tenant_scoped and (not mutating or write_scope)
    if admitted:
        assert authenticated and tenant_scoped
        if mutating:
            assert write_scope, "mutation admitted without write authority"
    if authenticated and tenant_scoped and not mutating:
        assert admitted, "read capability was unnecessarily denied"
    if mutating and not write_scope:
        assert not admitted
print("MCP capability lattice model: ok")
