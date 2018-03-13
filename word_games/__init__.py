from gym.envs.registration import register

register(
    id='LiarsDice-v0',
    entry_point='liars_dice.envs:LiarsDiceEnv',
)
