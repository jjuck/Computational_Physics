from vpython import *

# 지구와 달의 초기 위치와 속도
earth_pos = vector(0, 0, 0)
earth_v = vector(0, 0, 0)
moon_pos = vector(384.4e6, 0, 0)
moon_v = vector(0, 1023, 0)

# 지구와 달의 질량
earth_mass = 5.97e24
moon_mass = 7.35e22

# 중력 상수
G = 6.67e-11

# 지구 객체 생성
earth = sphere(pos=earth_pos, radius=6.4e6, texture=textures.earth)
earth.trail = curve(color=earth.color)
earth.m = earth_mass

# 달 객체 생성
moon = sphere(pos=moon_pos, radius=1.75e6, texture=textures.rock)
moon.trail = curve(color=moon.color)
moon.m = moon_mass

# 지구와 달의 확대를 위한 설정
earth.radius = 6 * earth.radius
moon.radius = 6 * moon.radius

# 시간 초기화
t = 0
dt = 60

while True:
    rate(1000)
    
    # 지구-달 사이의 거리 계산
    r = moon.pos - earth.pos
    
    # 중력 벡터 계산
    F = G * earth.m * moon.m / mag(r)**2 * norm(r)
    
    # 지구와 달에 대한 중력 가속도 계산
    earth_a = F / earth.m
    moon_a = -F / moon.m
    
    # 속도와 위치 업데이트
    earth_v += earth_a * dt
    moon_v += moon_a * dt
    earth.pos += earth_v * dt
    moon.pos += moon_v * dt
    
    # 궤적 업데이트
    earth.trail.append(pos=earth.pos)
    moon.trail.append(pos=moon.pos)
    
    # 시간 업데이트
    t += dt
