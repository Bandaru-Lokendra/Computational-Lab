def gen_sin(F) 
   t=0:0.01:1
   y=sin(2*pi*F*t)
   plot(t,y)
  return y
 y=gen_sin(5)