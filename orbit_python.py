scene.lights=[distant_light(direction=vec(1,0,0))]
scene.ambient=color.black
RE=6.37e6
ME = 5.972e24
h=400e3
G=6.67e-11

Earth=sphere(pos=vec(0,0,0), radius=RE, texture=textures.earth, shininess=0)
Earth.rotate(angle=pi/2, axis=vec(1,0,0),origin=vec(0,0,0))

omegaE=2*pi/(.997*24*60*60)

t=0
dt=10
ss=2000 #scale adjustment for Iss

iss=sphere(pos=(Earth.pos+vec(RE+h,0,0)), radius=ss*100, retain=350)
iss.m=1
attach_trail(iss, radius=.5*iss.radius)
viss=sqrt(G*ME/(RE+h))
iss.p=iss.m*vec(0,viss,0)

rgeo=(G*ME/omegaE**2)**(1./3.)
#satt=sphere(pos=(Earth.pos+vec(rgeo,0,0)), radius=ss*100, color=color.cyan)
#satt.m=1
#satt.p=satt.m*vector(0,rgeo*omegaE,0)
#attach_trail(satt)

while true:
    rate(100)
    Earth.rotate(angle=omegaE, axis=vec(0,0,1), origin=vec(0,0,0))
    r=iss.pos-Earth.pos
    Fiss=-G*ME*iss.m*norm(r)/mag(r)**2
    iss.p=iss.p+Fiss*dt
    iss.pos=iss.pos+iss.p*dt/iss.m
    
#    rsat=satt.pos-Earth.pos
#    Fsat=-G*ME*satt.m*norm(rsat)/mag(rsat)**2
#    satt.p=satt.p+Fsat*dt
#    satt.pos=satt.pos+satt.p/satt.m
    t=t+dt
