sx, sy, gx, gy = map(int, input().split())
x = gx - sx
y = gy - sy
print(f"{sx + (x / (sy + gy)) * sy:.10f}")
