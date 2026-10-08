#!/usr/bin/env python3
"""Sample fictional independent-image state; caller resolves scene suitability."""
import argparse, json, random
from pathlib import Path
catalog=json.loads((Path(__file__).resolve().parent.parent/'references/equipment-catalog.json').read_text())
choices=sorted({item['id'] for item in catalog['items']} | set(catalog['aliases']))
p=argparse.ArgumentParser()
p.add_argument('--equipment', nargs='+', choices=choices)
context=p.add_mutually_exclusive_group()
context.add_argument('--encounter', action='store_true', help='Use only after scene-rules encounter eligibility is verified.')
context.add_argument('--armed-exploration', action='store_true', help='Eligible urban player, no encounter: exploration/carry only.')
p.add_argument('--previous-money', type=int)
p.add_argument('--previous-equipment', choices=choices)
p.add_argument('--seed', type=int)
a=p.parse_args()
r=random.Random(a.seed)
n=r.randint(100,999999)
while n==a.previous_money:
    n=r.randint(100,999999)
firearms={item['id'] for item in catalog['items'] if item['category'] in ['handgun','shotgun','smg','assault-rifle','rifle']}
if a.encounter or a.armed_exploration:
    selected=a.equipment or ['fist','pistol-9mm','desert-eagle','smg','micro-smg','m4','ak-47']
else:
    selected=a.equipment or ['fist','camera','flowers']
eligible=list(dict.fromkeys(catalog['aliases'].get(item,item) for item in selected))
previous=catalog['aliases'].get(a.previous_equipment,a.previous_equipment)
if len(eligible)>1 and previous in eligible:
    eligible.remove(previous)
state={'money':f'${n:08d}'}
if a.encounter or a.armed_exploration:
    guns=[item for item in eligible if item in firearms]
    other=[item for item in eligible if item not in firearms]
    actions=[]; weights=[]
    if other: actions.append('exploration'); weights.append(60 if a.armed_exploration else 35)
    if guns:
        actions.append('armed-carry'); weights.append(40 if a.armed_exploration else 30)
        if a.encounter:
            actions.extend(['aiming','firing']); weights.extend([20,15])
    action=r.choices(actions,weights=weights,k=1)[0]
    state.update(equipment=r.choice(other if action=='exploration' else guns),action=action,
                 reticle=action in ['aiming','firing'],muzzle_flash=action=='firing')
else:
    state['equipment']=r.choice(eligible)
print(json.dumps(state))
