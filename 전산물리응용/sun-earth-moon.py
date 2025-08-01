from vpython import *

# 태양과 지구, 달의 초기 위치와 속도
sun_pos = vector(0, 0, 0)
sun_v = vector(0, 0, 0)
earth_pos = vector(149.6e9, 0, 0)
earth_v = vector(0, 29780, 0)
moon_pos = vector(149.6e9+384.4e6, 0, 0) # 지구와 동일한 y=0, z=0 위치에서 x축 방향으로 384,400km 떨어져 있음
moon_v = vector(0, 29780+1023, 0) # 지구와 동일한 초기 속도

# 태양과 지구, 달의 질량
sun_mass = 1.99e30
earth_mass = 5.97e24
moon_mass = earth_mass / 7.35e22

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

# 달 객체 생성
moon = sphere(pos=moon_pos, radius=1.74e6, texture=textures.rock)
moon.trail = curve(color=moon.color)
moon.m = moon_mass

# 지구와 태양, 달의 확대를 위한 설정
sun.radius = 30 * sun.radius
earth.radius = 1000 * earth.radius
moon.radius = 5000 * moon.radius

# 시간 초기화
t = 0
dt = 720

month=24*3600*28

while t<3*month:
    rate(1000)

    # 태양과 지구 사이의 거리 계산
    r_earth_sun = earth.pos - sun.pos

    # 태양과 달 사이의 거리 계산
    r_moon_sun = moon.pos - sun.pos

    # 지구와 달 사이의 거리 계산
    r_moon_earth = moon.pos - earth.pos

    # 중력 벡터 계산
    F_earth_sun = G * sun.m * earth.m / mag(r_earth_sun) ** 2 * norm(r_earth_sun)
    F_moon_sun = G * sun.m * moon.m / mag(r_moon_sun) ** 2 * norm(r_moon_sun)
    F_moon_earth = G * earth.m * moon.m / mag(r_moon_earth) ** 2 * norm(r_moon_earth)

    # 지구와 달에 대한 중력 가속도 계산
    sun_a = (F_earth_sun + F_moon_sun) / sun.m
    earth_a = - (F_earth_sun - F_moon_earth) / earth.m
    moon_a = - (F_moon_earth + F_moon_sun) / moon.m

    # 속도와 위치 업데이트
    earth_v += earth_a * dt
    sun_v += sun_a * dt
    moon_v += moon_a * dt
    earth.pos += earth_v * dt
    sun.pos += sun_v * dt
    moon.pos += moon_v * dt

    # 궤적 업데이트
    earth.trail.append(pos=earth.pos)
    sun.trail.append(pos=sun.pos)
    moon.trail.append(pos=moon.pos)

    # 시간 업데이트
    t += dt
