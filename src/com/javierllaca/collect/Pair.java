package com.javierllaca.collect;

/**
 * Pair, or 2-tuple, data structure
 * @author Javier Llaca
 */
public class Pair<F,S> {

  private F first;
  private S second;

  public Pair(F f, S s) {
    this.first = f;
    this.second = s;
  }

  public F first() {
    return this.first;
  }

  public S second() {
    return this.second;
  }

  public String toString() {
    return "(" + this.first.toString() + 
      ", " + this.second.toString() + ")";
  }
}
