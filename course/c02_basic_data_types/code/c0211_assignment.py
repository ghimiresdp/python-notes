# https://sudipghimire.com.np
"""
Assignment operations:
    =
    +=
    -=
    *=
    /=
    %=
    //=
    **=
    &=
    |=
    ^=
    >>=
    <<=
"""

# %% = operator
x = 50
print(x)

x, y = 5, 10
# %% += operator

x += 2      # x = x + 2
print(x)

# %% -= operator

x -= 2      # x = x - 2
print(x)

# %% *= operator
x *= 3      # x = x * 2
print(x)

# %%    /= operator
x /= 3      # x = x / 2
print(x)

# %% %= operator

x %= 30     # x = x % 30
print(x)
# %% //= operator

x //= 2     # x = x // 2
print(x)

# %% **= operator

x **= 5     # x = x ** 2
print(x)

# %% &= operator
x = 5       # 101
x &= 6      # 110       # x = x & 2
print(x)    # 100

# %% |= operator
x = 5       # 101
x |= 6      # 110       # x = x | 2
print(x)    # 111

# %% ^= operator
x = 5       # 101
x ^= 6      # 110       # x = x ^ 2
print(x)    # 011

# %% >>= operator
x = 5       # 0000 0101
x >>= 1     # -> shift right 1 time     # x = x >> 1
print(x)    # [ 0000 0010 ] 1 <- this is discarded

# %% <<= operator
x = 5       # 0000 0101
x <<= 2     # <- shift left 2 times     # x = x << 2
print(x)    # 00[00 010100] <- 2 more zeros added in the end

# %%
