from flask_restful import Resource
import requests;
import os;

from flask import Flask, jsonify, json


class ApiHandler(Resource):
  
  def get(self):
      url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
      Twitter_Barear_Token= os.environ.get('Twitter_Barear_Token')

      header = {"Authorization":  f"Bearer {Twitter_Barear_Token}"}
      userName = "emanWamda" #requests.args.get("searchQuery")
      params = {'screen_name': userName};
      response = requests.get(url, headers= header, params = params)

      if response.status_code != 200 :
          raise Exception(
              "Request returned an error: {} {}".format(
              response.status_code, response.text    
              )
          )

      print('tweets');
      tweets = response.json();

      dict = {};
      for x in tweets: 
            if x['text'] in dict: 
                ++dict[x['text']]
            else:
               dict[x['text']]= 1

      max_word= ""       
      max = 0    
      for key in dict.keys(): 
        if dict[key] > max:
            max = dict[key]
            max_word = key

      print(max)
      return jsonify({'text': max, 'value': max_word})
    