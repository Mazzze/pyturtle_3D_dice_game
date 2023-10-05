import turtle, math, random
screen = turtle.getscreen()
turtle.ht()
lie = turtle.Turtle()
lie.ht()
lie.speed(0)

backt = turtle.Turtle()
backt.ht()
backt.speed(0)

txt = turtle.Turtle()
txt.ht()
txt.pu()
txt.speed(0)

u = 500
z_glo = 0.1

bordlvl = -40*u
compens = -bordlvl*0.115
bord_x_side = 4
bord_z_side = 10*z_glo

lamp_y = bordlvl+u*20
lamp_x = 7.2*u
lamp_z = 9.8
lamp_pos = [lamp_x,lamp_y,lamp_z]
light_pole = False

dice_demo_num = 3
dice_color = 0


colors = ['dark blue','gray','dark green','dark red']
colors_top = ['blue','white','green','red']

text_pos = (0,1*u)

def draw_tabel():
  bord_x_side_spawn = bord_x_side + 2.5
  bord_z_side_spawn = bord_z_side + 0.5
  compens_spawn = -bordlvl*0.113

  A = (-bord_x_side_spawn*u/8,bordlvl/8+compens_spawn)
  B = (bord_x_side_spawn*u/8,bordlvl/8+compens_spawn)
  C = (bord_x_side_spawn*u/(bord_z_side_spawn+8),bordlvl/(bord_z_side_spawn+8)+compens_spawn)
  D = (-bord_x_side_spawn*u/(bord_z_side_spawn+8),bordlvl/(bord_z_side_spawn+8)+compens_spawn)

  go_board = [A,B,C,D]
  backt.pu()
  backt.goto(D)
  backt.pd()
  backt.fillcolor('purple')
  backt.begin_fill()
  for i in go_board:
    backt.goto(i)
  backt.end_fill()

def draw_tabel_spawn():
  A = convert(-bord_x_side*u,bordlvl,8)
  B = convert(bord_x_side*u,bordlvl,8)
  C = convert(bord_x_side*u,bordlvl,(bord_z_side+8))
  D = convert(-bord_x_side*u,bordlvl,bord_z_side+8)

  go_board = [A,B,C,D]
  backt.pu()
  backt.goto(D)
  backt.pd()
  for i in go_board:
    backt.goto(i)

def convert(x_con,y_con,z_con):
  re = ((x_con/z_con,y_con/z_con+compens))
  return re

def light_bulb_draw(lamp_pos):
  backt.ht()
  cu = u*0.03
  backt.pu()
  backt.goto(convert(lamp_pos[0],lamp_pos[1],lamp_pos[2]))

  backt.seth(90)
  backt.fd(cu)
  backt.seth(180)
  backt.circle(cu,75)
  pos_var_one = backt.pos()
  backt.fillcolor('yellow')
  backt.begin_fill()
  backt.pd()
  backt.circle(cu,225)
  backt.circle(-cu,30)
  backt.fd(cu*0.35)
  backt.circle(cu*0.2,90)
  pos_var_two = backt.pos()
  backt.fd(cu*1.1)
  pos_var_three = backt.pos()
  backt.circle(cu*0.2,90)
  backt.fd(cu*0.35)
  backt.circle(-cu,30)
  backt.goto(pos_var_one)
  backt.end_fill()

  backt.pu()
  backt.goto(pos_var_three)
  backt.fillcolor('grey')
  backt.begin_fill()
  backt.goto(pos_var_two)
  backt.seth(90)
  backt.pd()
  backt.circle(cu*0.1,90)
  backt.circle(-cu*0.1,180)
  backt.circle(cu*0.1,-180)
  backt.circle(-cu*0.1,45)
  backt.circle(cu*0.1,45)
  pos_var_four = backt.pos()

  backt.pu()
  backt.goto(pos_var_three)
  backt.seth(270)
  backt.pd()
  backt.circle(cu*0.1,-90)
  backt.circle(-cu*0.1,-180)
  backt.circle(cu*0.1,180)
  backt.circle(-cu*0.1,-45)
  backt.circle(cu*0.1,-45)
  backt.goto(pos_var_four)
  backt.pu()
  backt.goto(pos_var_three)
  backt.end_fill()
  
  if light_pole == True:
    backt.pu()
    backt.goto(convert(lamp_pos[0],lamp_pos[1],lamp_pos[2]))
    backt.pd()
    backt.goto(convert(lamp_pos[0],bordlvl,lamp_pos[2]))

class dice: 
  def __init__(self,D_pos,vink):
    self.x_a = D_pos[0]
    self.y_a = D_pos[1]
    self.z_a = D_pos[2]
    self.vink_cube = vink
    xp = D_pos[0]
    yp = D_pos[1]
    zp = D_pos[2]

    u_sin = (u*math.sin(vink))
    u_cos = (u*math.cos(vink))
    z_sin = (z_glo*math.sin(vink))
    z_cos = (z_glo*math.cos(vink))

    self.a = convert(xp,yp,zp)
    self.b = convert((xp-u_cos),yp,(zp-z_sin))
    self.c = convert((xp-u_sin-u_cos),yp,(zp+z_cos-z_sin))
    self.d = convert((xp-u_sin),yp,(zp+z_cos))

    self.e = convert(xp,yp+u,zp)
    self.f = convert((xp-u_cos),yp+u,(zp-z_sin))
    self.g = convert((xp-u_sin-u_cos),yp+u,(zp+z_cos-z_sin))
    self.h = convert((xp-u_sin),yp+u,(zp+z_cos))

    self.color_num = random.randint(0,len(colors)-1)

def skugg_calc(x_in,y_in,z_in):
  kx = (lamp_y-y_in)/(lamp_x-x_in)
  kz = (lamp_y-y_in)/(lamp_z-z_in)/(u*10)
  xu = x_in-u/(kx)
  zu = z_in-z_glo/(kz)

  return convert(xu,bordlvl,zu)

def dra_cube(dice):
  lie.pu()
  lie.goto(dice.a)
  print(dice.a)
  lie.pd()
  lie.goto(dice.b)
  lie.goto(dice.c)
  lie.goto(dice.d)
  lie.goto(dice.a)
  lie.goto(dice.e)
  lie.goto(dice.f)
  lie.goto(dice.b)
  lie.goto(dice.f)
  lie.goto(dice.g)
  lie.goto(dice.c)
  lie.goto(dice.g)
  lie.goto(dice.h)
  lie.goto(dice.d)
  lie.goto(dice.h)
  lie.goto(dice.e)
##################################################
def dice_side_five(a,b,c,d,num):
  def cord_dot_mesure(p_one,p_two,part):
    return (p_one[0]-((p_one[0]-p_two[0])/10)*part,p_one[1]-((p_one[1]-p_two[1])/10)*part)

  def cord_meta(dot_x,dot_y):
    return cord_dot_mesure( cord_dot_mesure(a,d,dot_y) ,cord_dot_mesure(b,c,dot_y) ,dot_x )

  x_u = (a[0]-b[0])/10
  y_u = (a[1]-d[1])/10
  vink_diamond = math.atan2((a[1]-d[1]),(a[0]-b[0]))
  print(vink_diamond,'vink_diamond',math.sin(vink_diamond),math.cos(vink_diamond))


  def Ddot(center_point):
    si = math.sin(vink_diamond)
    co = math.cos(vink_diamond)
    sizd = 0.7
    top_d = (center_point[0]-sizd*x_u,center_point[1]-sizd*y_u)
    left_d = (center_point[0]+sizd*x_u,center_point[1]-sizd*y_u)
    bot_d = (center_point[0]+sizd*x_u,center_point[1]+sizd*y_u)
    right_d = (center_point[0]-sizd*x_u,center_point[1]+sizd*y_u)
    dot_path = [left_d,bot_d,right_d]

    lie.pu()
    lie.goto(top_d)
    lie.begin_fill()
    lie.fillcolor('black')
    for i in dot_path:
      lie.goto(i)
    lie.end_fill()

  lie.goto(a)

  if num == 1:
    Ddot(cord_meta(5,5))

  elif num == 2:
    Ddot(cord_meta(2,8))
    Ddot(cord_meta(8,2))
  
  elif num == 3:
    Ddot(cord_meta(2,8))
    Ddot(cord_meta(5,5))
    Ddot(cord_meta(8,2))

  elif num == 4:
    Ddot(cord_meta(2,8))
    Ddot(cord_meta(8,8))
    Ddot(cord_meta(2,2))
    Ddot(cord_meta(8,2))

  elif num == 5:
    Ddot(cord_meta(2,8))
    Ddot(cord_meta(8,8))
    Ddot(cord_meta(2,2))
    Ddot(cord_meta(8,2))
    Ddot(cord_meta(5,5))

  elif num == 6:
    Ddot(cord_meta(2,8))
    Ddot(cord_meta(8,8))
    Ddot(cord_meta(2,5))
    Ddot(cord_meta(8,5))
    Ddot(cord_meta(2,2))
    Ddot(cord_meta(8,2))
###########################################

def fill_front(dice):
  lie.goto(dice.a)
  lie.fillcolor(colors[dice.color_num])
  lie.begin_fill()
  lie.goto(dice.b)
  lie.goto(dice.f)
  lie.goto(dice.e)
  lie.end_fill()

def fill_right(dice):
  lie.goto(dice.a)
  lie.fillcolor(colors[dice.color_num])
  lie.begin_fill()
  lie.goto(dice.e)
  lie.goto(dice.h)
  lie.goto(dice.d)
  lie.end_fill()

def fill_left(dice):
  lie.goto(dice.b)
  lie.fillcolor(colors[dice.color_num])
  lie.begin_fill()
  lie.goto(dice.f)
  lie.goto(dice.g)
  lie.goto(dice.c)
  lie.end_fill()

def fill_top(dice):
  lie.goto(dice.e)
  lie.fillcolor(colors_top[dice.color_num])
  lie.begin_fill()
  lie.goto(dice.f)
  lie.goto(dice.g)
  lie.goto(dice.h)
  lie.end_fill()

def fill_back(dice):
  lie.goto(dice.d)
  lie.fillcolor(colors[dice.color_num])
  lie.begin_fill()
  lie.goto(dice.h)
  lie.goto(dice.g)
  lie.goto(dice.c)
  lie.end_fill()

def skugg_draw(dice,xp,yp,zp):
  u_sin = (u*math.sin(dice.vink_cube))
  u_cos = (u*math.cos(dice.vink_cube))
  z_sin = (z_glo*math.sin(dice.vink_cube))
  z_cos = (z_glo*math.cos(dice.vink_cube))

  e = skugg_calc(xp,(yp+u),zp)
  f = skugg_calc((xp-u_cos),(yp+u),(zp-z_sin))
  g = skugg_calc((xp-u_sin-u_cos),(yp+u),(zp+z_cos-z_sin))
  h = skugg_calc((xp-u_sin),(yp+u),(zp+z_cos))

  skugg_list = [[dice.a,dice.b,f,e,dice.a],[dice.b,dice.c,g,f,dice.b],[dice.c,dice.d,h,g,dice.c],[dice.a,dice.d,h,e,dice.a]]

  lie.pu()
  for i in skugg_list:
    lie.fillcolor('black')
    lie.begin_fill()
    for j in i:
      lie.goto(j)
    lie.end_fill()

def doted_front(dice,num):
  side_num = [0,5,6,1,2,3,4]
  lie.goto(dice.a)
  lie.fillcolor("gray")
  lie.begin_fill()
  lie.goto(dice.b)
  lie.goto(dice.f)
  lie.goto(dice.e)
  lie.end_fill()
  dice_side_five(dice.a,dice.b,dice.f,dice.e,side_num[num])

def doted_right(dice,num):
  side_num = [0,3,4,5,6,1,2]
  lie.goto(dice.a)
  lie.fillcolor("gray")
  lie.begin_fill()
  lie.goto(dice.e)
  lie.goto(dice.h)
  lie.goto(dice.d)
  lie.end_fill()
  dice_side_five(dice.a,dice.d,dice.h,dice.e,side_num[num])

def doted_left(dice,num):
  side_num = [0,3,4,5,6,1,2]
  lie.goto(dice.b)
  lie.fillcolor("gray")
  lie.begin_fill()
  lie.goto(dice.f)
  lie.goto(dice.g)
  lie.goto(dice.c)
  lie.end_fill()
  dice_side_five(dice.b,dice.c,dice.g,dice.f,7-side_num[num])

def doted_top(dice,num):
  lie.goto(dice.e)
  lie.fillcolor("white")
  lie.begin_fill()
  lie.goto(dice.f)
  lie.goto(dice.g)
  lie.goto(dice.h)
  lie.end_fill()
  dice_side_five(dice.e,dice.f,dice.g,dice.h,num)

def doted_back(dice,num):
  side_num = [0,5,6,1,2,3,4]
  lie.goto(dice.d)
  lie.fillcolor("gray")
  lie.begin_fill()
  lie.goto(dice.h)
  lie.goto(dice.g)
  lie.goto(dice.c)
  lie.end_fill()
  dice_side_five(dice.d,dice.c,dice.g,dice.h,7-side_num[num])

def fill_sides(dice,re_pos,num):
  T_v = re_pos[2] + math.atan(re_pos[0]/re_pos[1])
  if T_v>360:
    T_v-=360
  elif T_v<0:
    T_v=360
  print('T-v', T_v)
  lie.pu()
  if dice_color >= 0.1:
    if T_v>= 0 and T_v<=90:
      #fill_back(dice)
      #fill_right(dice)
      fill_left(dice)
      fill_front(dice)

    elif T_v>=90 and T_v<=135:
      #fill_right(dice)
      #fill_front(dice)
      fill_back(dice)
      fill_left(dice)
    
    elif T_v>=135 and T_v<=180:
      #fill_front(dice)
      fill_left(dice)
      #fill_right(dice)
      fill_back(dice)

    elif T_v>=180 and T_v<=270:
      #fill_front(dice)
      #fill_left(dice)
      fill_right(dice)
      fill_back(dice)

    elif T_v>=270 and T_v<=360:
      #fill_left(dice)
      #fill_back(dice)
      fill_front(dice)
      fill_right(dice)
    fill_top(dice)
  
  else:
    if T_v>= 0 and T_v<=90:
      #doted_back(dice,num)
      #doted_right(dice,num)
      doted_left(dice,num)
      doted_front(dice,num)

    elif T_v>=90 and T_v<=135:
      #doted_right(dice,num)
      #doted_front(dice,num)
      doted_back(dice,num)
      doted_left(dice,num)
    
    elif T_v>=135 and T_v<=180:
      #doted_front(dice,num)
      doted_left(dice,num)
      #doted_right(dice,num)
      doted_back(dice,num)

    elif T_v>=180 and T_v<=270:
      #doted_front(dice,num)
      #doted_left(dice,num)
      doted_right(dice,num)
      doted_back(dice,num)

    elif T_v>=270 and T_v<=360:
      #doted_left(dice,num)
      #doted_back(dice,num)
      doted_front(dice,num)
      doted_right(dice,num)
    doted_top(dice,num)

def custom_sort(t):
    return t[1]

def multi_cube_pos(pos_list,amount):
  for i in range(amount):
    x_pos = (2*bord_x_side * random.random() - bord_x_side)*u
    z_pos = bord_z_side*random.random() + 8
    vink = random.randint(0,45)
    pos_list.append([x_pos,z_pos,vink])
  print(pos_list)
  
  pos_list.sort(key = custom_sort, reverse = True) 
  
  print(pos_list)

def throw_cube(dice_num):
  pos_list = []
  multi_cube_pos(pos_list,len(dice_num))
  for i in range(len(dice_num)):
    print('dice nr',i+1,pos_list)
    p1 = dice([pos_list[i][0],bordlvl,pos_list[i][1]],math.radians(pos_list[i][2]))
    dra_cube(p1)
    skugg_draw(p1,pos_list[i][0],bordlvl,pos_list[i][1])
    fill_sides(p1,pos_list[i],dice_num[i])

def demo_list(num):
  re = []
  for i in range(num):
    re.append(random.randint(1,6))
  return re

draw_tabel()
#draw_tabel_spawn()
light_bulb_draw(lamp_pos)

if dice_demo_num >= 0.1:
  dice_num = demo_list(dice_demo_num)
  throw_cube(dice_num)

if dice_color >= 0.1:
  dice_num = demo_list(dice_color)
  throw_cube(dice_num)
"""
def klick():
  throw_cube(dice_num)
def klicktwo():
  lie.clear()

screen.onkey(klick,'a')
screen.onkey(klicktwo,'d')
screen.listen()
"""

############################    GAME    ###################################


def textw(texsting,clear_or,row):
  if clear_or == True:
    txt.clear()
  txt.goto(text_pos[0],text_pos[1]-row*u/10)
  txt.write(texsting, True, align="center",font=("Arial", 0.08*u, "normal"))

def throw(num):
  dices = []
  for i in range(num):
    dices.append(random.randint(1,6))
  return dices

def options(kast):
  pot_saves = []
  mult_skip = []
  for i in range(6):
    multipel = []
    for j in kast:
      if j == i+1:
        multipel.append(j)
    if len(multipel) >= 3:
      mult_skip.append(int(sum(multipel)/len(multipel)))
      pot_saves.append(multipel)

  for i in kast:
    if i in mult_skip:
      pass
    elif i == 1 or i == 5:
      pot_saves.append(i)
    elif kast == [1,2,3,4,5]:
      return([12345])
    elif kast == [2,3,4,5,6]:
      return([23456])

  return pot_saves


def save_klick_all():
  global save_pre
  save_pre = 'all'


#the funktion that is used to chose what dices is to be saved PLAYER
def save_funk(opt):
  def save_inerfunk(opt):
    textw('save << key',True,0)
    save = 0
    save_pre = 0
    for i in range(len(opt)):
      textw((opt[i],'<<',i+1),False,i+1)

    textw('All << a',False,len(opt)+1)
    screen.onkey(save_klick_all,'a')
    screen.listen()
    if save_pre == 'all':
      save = []
      for i in range(len(opt)):
        save.append(str(i+1))
      return save
    #save = save.split()
    screen.listen()
    #return save
  save_meta = save_inerfunk(opt)
  if save_meta == None:
    save_meta = save_inerfunk(opt)
  else:
    return save_meta

#Save funktion but for ALGORITHM --- saves all
def keda_save_funk(opt):
  print('\nsave << key')
  for i in range(len(opt)):
    print(opt[i],'<<',i+1)

  save = []
  for i in range(len(opt)):
    save.append(str(i+1))

  return save

#Funktion that dicides how many points player saves are woth
def point(choise,tempo_point,dice_remo):  
  #print(choise) #bug check
  if choise == 1 or choise == 5:
    dice_remo-=1
    tempo_point+=50   
  elif choise == 12345:
    dice_remo-=5
    tempo_point+=800
  elif choise == 23456:
    dice_remo-=5
    tempo_point+=1000 
  elif choise != int:
    if len(choise) >= 3:
      tempo_point+=int(sum(choise)/len(choise)*100*2**(len(choise)-3))
      for i in range(len(choise)):
        dice_remo-=1 

  ret = [tempo_point,dice_remo]

  return ret


#kast = [1,2,3,4,5]
#kast = [2,3,4,5,6]
#kast = [1,5,5,5,5]
#kast = [2,5,5,5,5]

#Two player funktion throw
def complete(num, tempo_point,player):
  kast = throw(num)
  lie.clear()
  throw_cube(kast)
  kast.sort()
  print(player,'Throw')
  opt = options(kast)
  if opt == []:
    print('\n!!!!!!!!!!!!!!!!!!',player,'---No luck!!!!!!!!!!!!!!!\n')
    return 0
  save = save_funk(opt)
  dice_remo = num
  print('save',save)
  for i in save:
    i=int(i)-1
    ret = point(opt[int(i)],tempo_point,dice_remo)
    tempo_point = ret[0]
    dice_remo = ret[1]
  print(player,'\nPoints',tempo_point,'dices', dice_remo,'left')

  if dice_remo == 0:
    return tempo_point

  print('\n',player)
  proside = int(input('\nThrow again << 1 \nStay and save points << 2\n\n<<'))
  
  if proside == 2:
    print(tempo_point)
    return tempo_point
  else:
    return complete(dice_remo,tempo_point,player)

#ALG funktion for thorw in singel_player_alg
def alg(num,tempo_point,you,keda,goal):
  kast = throw(num)
  kast.sort()
  print('Keda -- Throw')
  opt = options(kast)
  if opt == []:
    print('\n!!!!!!!!!!!!!!!!!!Keda---No luck!!!!!!!!!!!!!!!\n')
    return 0
  save = keda_save_funk(opt)
  dice_remo = num

  for i in save:
    i=int(i)-1
    ret = point(opt[int(i)],tempo_point,dice_remo)
    tempo_point = ret[0]
    dice_remo = ret[1]
  print('Keda\nPoints',tempo_point,'dices', dice_remo,'left')

  if you>=goal and dice_remo!=0 and keda+tempo_point<=goal:
    print('Keda tries again')
    return alg(dice_remo,tempo_point,you,keda,goal)

  elif dice_remo == 0 or keda+tempo_point>=goal or keda>=you:
    print(tempo_point,' points Keda stays')
    return tempo_point
  else:
    print('Keda tries again')
    return alg(dice_remo,tempo_point,you,keda,goal)


#---------------gamemodes-------------  

def two_player():
  you = 0
  keda = 0
  goal = 800
  dice = 5
  while you <= goal and keda <= goal:
    you+=complete(dice,0,'You')
    print('------you--',you,'------\n\n')
    keda+=complete(dice,0,'Keda')
    print('------Keda--',keda,'------\n\n')
  if keda >= you:
    print('Keda Win')
  else:
    print('You Win')

def singel_player_alg():
  you = 0
  keda = 0
  goal = 800
  dice = 5
  while you <= goal and keda <= goal:
    you+=complete(dice,0,'You')
    print('------you--',you,'------\n\n')
    keda+=alg(dice,0,you,keda,goal)
    print('------Keda--',keda,'------\n\n')
  if keda >= you:
    print('Keda Win')
  else:
    print('You Win')

def alg_alg():
  Beda = 0
  keda = 0
  goal = 800
  dice = 5
  while Beda <= goal and keda <= goal:
    keda+=alg(dice,0,Beda,keda,goal)
    print('------you--',Beda,'------\n\n')
    Beda+=alg(dice,0,keda,Beda,goal)
    print('------Keda--',keda,'------\n\n')
  if keda >= Beda:
    print('Keda Win')
    return 1
  else:
    print('Beda Win')
    return 0

#singel_player_alg()
def super_alg(times):
  keda_wins = 0
  for i in range(times):
    keda_wins+=alg_alg()
  print('keda',keda_wins,' --- Beda',times-keda_wins)


val = int(input('Välj \nKeda vs Beda << 1 \nYou vs Keda << 2\n>>'))
if val == 1: 
  gngr = int(input('How many times\n>>'))
  super_alg(gngr)
else:
  singel_player_alg()