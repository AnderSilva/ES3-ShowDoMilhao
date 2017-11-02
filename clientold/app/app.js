'use strict';

// Declare app level module which depends on views, and components
angular.module('myApp', [
  'ngRoute',
  'ngMaterial',
  'ngAria',
  'ngAnimate',
  'myApp.view1',
  'myApp.view2',
  'myApp.signUp',
  'myApp.signIn',
  'myApp.map',
  'myApp.quiz',
  'myApp.shop',
  'myApp.admin',
  'myApp.version'
]).
config(['$locationProvider', '$routeProvider', function($locationProvider, $routeProvider) {
  $locationProvider.hashPrefix('!');
  $routeProvider.otherwise({redirectTo: '/view1'});
}]);
