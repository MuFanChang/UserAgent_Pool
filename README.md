# UserAgentPool
This is modified from Fake-UserAgent ,Just for private use.

# Install
  in command line:
  
    pip install UserAgent_Pool
# How to use
  in python environment:
    
    from UserAgent_Pool.UserAgentPool import UserAgent
    
    ua = UserAgent()
    
  and you can use the function inside the UserAgent()
# Functions

    UserAgent().random 
  → It'll randomly choose one header from the Total Pool 
  
    UserAgent().chrome
    UserAgent().opera
    UserAgent().firefox
    UserAgent().ie
    UserAgent().safari
  → It'll randomly choose one header from Specific Pool
  
