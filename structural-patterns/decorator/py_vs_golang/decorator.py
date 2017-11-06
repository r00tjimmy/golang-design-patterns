#coding=utf-8
import sys

def cache(fib):
  temp = {}
  def _cache(n):
    if n not in temp:
      temp[n] = fib(n)
    return temp[n]
  return _cache


@cache
def fib(n):
  if n < 2:
    return n
  else:
    return fib(n-2) + fib(n-1)


if len(sys.argv) == 2:
  print fib(int(sys.argv[1]))
else:
  print "input"