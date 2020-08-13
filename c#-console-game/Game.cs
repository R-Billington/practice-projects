using System;

namespace ConsoleGame
{
  class Game : SuperGame
  {
    public new static void UpdatePosition(string key, out int xChange, out int yChange)
    {   
        switch (key)
        {
            case "DownArrow":
                xChange = 0;
                yChange = 1;
                break;
            case "UpArrow":
                xChange = 0;
                yChange = -1;
                break;
            case "LeftArrow":
                xChange = -1;
                yChange = 0;
                break;
            case "RightArrow":
                xChange = 1;
                yChange = 0;
                break;
            default:
                xChange = 0;
                yChange = 0;
                break;
        }
    }
    
    public new static char UpdateCursor(string key)
    {
        switch (key)
        {
            case "DownArrow":
                return 'v';
            case "UpArrow":
                return '^';
            case "LeftArrow":
                return '<';
            case "RightArrow":
                return '>';
            default:
                return '<';
        }
    }
    
    public new static int KeepInBounds(int coord, int maxValue)
    {
        if (coord < 0)
        {
            return 0;
        }
        else if (coord >= maxValue)
        {
            return maxValue - 1;
        }
        else
        {
            return coord;
        }
    }
    
    public new static bool DidScore(int xPlayer, int yPlayer, int xFruit, int yFruit)
    {
        if (xPlayer == xFruit && yPlayer == yFruit)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
  }
}












