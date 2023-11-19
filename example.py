from cengal_memory_barriers import full_memory_barrier

full_memory_barrier()

import os
if 'nt' != os.name:
    from cengal_memory_barriers import py_atomic_thread_fence, MEMORY_ORDER_RELAXED

    py_atomic_thread_fence(MEMORY_ORDER_RELAXED)
