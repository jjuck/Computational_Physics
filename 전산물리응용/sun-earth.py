from vpython import *

# 태양과 지구의 초기 위치와 속도
sun_pos = vector(0, 0, 0)
sun_v = vector(0, 0, 0)
earth_pos = vector(149.6e9, 0, 0)
earth_v = vector(0, 29780, 0)

# 태양과 지구의 질량
sun_mass = 1.99e30
earth_mass = 5.97e24

# 중력 상수
G = 6.67e-11

# 태양 객체 생성
sun = sphere(pos=sun_pos, radius=6.96e8, color=color.red)
sun.trail = curve(color=sun.color)
sun.m = sun_mass

# 지구 객체 생성
earth = sphere(pos=earth_pos, radius=6.4e6, texture=textures.earth)
earth.trail = curve(color=earth.color)
earth.m = earth_mass

# 지구와 태양의 확대를 위한 설정
sun.radius = 30 * sun.radius
earth.radius = 1000 * earth.radius

# 시간 초기화
t = 0
dt = 360

month=24*3600*28

while t<month:
    rate(1000)
    
    # 지구-태양 사이의 거리 계산
    r = earth.pos - sun.pos
    
    # 중력 벡터 계산
    F = G * sun.m * earth.m / mag(r)**2 * norm(r)
    
    # 지구에 대한 중력 가속도 계산
    sun_a = F / sun.m
    earth_a = -F / earth.m
    
    # 속도와 위치 업데이트
    earth_v += earth_a * dt
    sun_v += sun_a * dt
    earth.pos += earth_v * dt
    sun.pos += sun_v * dt
    
    # 궤적 업데이트
    earth.trail.append(pos=earth.pos)
    sun.trail.append(pos=sun.pos)
    
    # 시간 업데이트
    t += dt
    