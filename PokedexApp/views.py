# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import requests
import json


# Create your views here.


def index(request, offset=0):
    page = int(request.GET.get("page", 1))
    
    paget=page-1
    offset = paget*10
    print(offset)
    #print(results)
    args= {'offset': offset} if offset else {}
    response = requests.get('https://pokeapi.co/api/v2/pokemon/?limit=10', params=args)
    payload = response.json()
    results = payload.get('results', [])
    

    lista_pokemones=[]
    for result in results:
        urlP = result["url"]
        #print(urlP)

        response = requests.get(urlP)
        payload = response.json()
        #print (payload)

        pokemon={
            'name': payload.get("name", ""),
            'id': payload.get("id", ""),
            'sprite' : payload.get("sprites", "").get("other", "").get("official-artwork", "").get("front_default", "")
        }
        lista_pokemones.append(pokemon)
    
            
    return render(request, "index.html", {'lista_pokemones': lista_pokemones, 
        "pagination": { 
            "page": page, 
            "prev_page": page - 1 if page > 1 else page, 
            "next_page": page + 1, 
            }})
    pass






def ver_pokemon(request, pk):
    id=pk
    
    
    response = requests.get('https://pokeapi.co/api/v2/pokemon/%s' % id)
    payload = response.json()

    sprite=payload.get("sprites", "").get("other", "").get("official-artwork", "").get("front_default", "")
    name=payload['name']
    peso=payload['weight']
    altura=payload['height']
    tipos=payload['types']
    habilidades=payload['abilities']
    movimientos=payload['moves']
    types = [types['type']['url'] for types in payload['types']]
    print(types)

    
    #return HttpResponse(sprite)
    return render(request, "ver_pokemon.html", {'sprite': sprite, 'name': name, 'altura': altura, 'peso': peso, 'tipos': tipos, 'habilidades': habilidades, 'movimientos': movimientos})
        

        

def tipo_pokemon(request, types):
    

        
    response = requests.get('https://pokeapi.co/api/v2/type/%s' % types)
    payload = response.json()
    results=payload['pokemon']
    #print(results)

    lista_pokemones=[]
    for result in results:
        urlP = result["pokemon"]["url"]
        #print(urlP)
        response = requests.get(urlP)
        payload = response.json()
        pokemon={
            'name': payload.get("name", ""),
            'id': payload.get("id", ""),
            'sprite' : payload.get("sprites", "").get("other", "").get("official-artwork", "").get("front_default", "")
        }
        lista_pokemones.append(pokemon)
    
        
        
    return render(request, "index.html", {'lista_pokemones': lista_pokemones})
        



