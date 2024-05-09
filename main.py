# This file is for strategy

from util.objects import *
from util.routines import *
import random
from util.tools import find_hits


class Bot(GoslingAgent):
    # This function runs every in-game tick (every time the game updates anything)
    def run(self):
        if self.get_intent() is not None:
           return
        if self.kickoff_flag:
            self.set_intent(kickoff())
            return
        targets = {
            'at_opponent_goal': (self.foe_goal.left_post, self.foe_goal.right_post),
            'away_from_our_net': (self.friend_goal.right_post, self.friend_goal.left_post),
        }
        
        
        if self.distance_between(self.ball.location, self.friend_goal.location) < 1500:
            self.set_intent(goto(self.friend_goal.location))
            print("DEFEND FROM THE BALL!")
            return
        
        if self.me.boost > 15:
            hits = find_hits(self, targets)
            if len(hits['at_opponent_goal']) > 0:
                    self.set_intent(hits['at_opponent_goal'][0])
                    print("at opponent goal")
                    return
            if len(hits['away_from_our_net']) > 0:
                    self.set_intent(hits['away_from_our_net'][0])
                    print("away from our net")
                    return
            
        target_boost = self.get_closest_large_boost()
        if target_boost is not None:
                    self.set_intent(goto(target_boost.location))
                    print("GOING FOR BOOST")
                    return    

        
    
       
            
        
        