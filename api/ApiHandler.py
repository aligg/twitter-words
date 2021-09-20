from flask_restful import Resource
import requests;
import os;

from flask import Flask, jsonify, json


class ApiHandelr(Resource):
  url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
  Twitter_Barear_Token= os.environ.get('Twitter_Barear_Token')

  header = {"Authorization":  f"Bearer {Twitter_Barear_Token}"}
  def getTweets(self):
      userName = requests.args.get("userName")
      searchWord=  requests.args.get("word")
      params = {'screen_name': userName};
      response = requests.get(url, auth= header, params = params)

      if response.status_code != 200 :
          raise Exception(
              "Request returned an error: {} {}".format(
              response.status_code, response.text    
              )
          )

      print('tweets');
      tweets = response.json();
      tweet_obj = json.loads(tweets)
      tweets_filter = [x for x in tweet_obj if x['text'].find(searchWord) != -1]

      countOfTweets= len(tweets_filter)


      return jsonify({'text': searchWord, 'value': countOfTweets});
