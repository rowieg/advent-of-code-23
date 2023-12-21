def run():
  print("")
  
  
def flip_flop_module(pulse: str) -> str:
  on = False
  if pulse is "low":
    on = not on
    
  if on is True: return 
  if on is False: return
  return 0

def conjunction_module(pulse: str) -> str:
  return 0

def broadcast_module(pulse: str) -> str:
  return 0

def button_module(pulse: str) -> str:
  return 0