class Integer

  def to_roman
    roman = {
        1 => "I",
        4 => "IV",
        5 => "V",
        9 => "IX",
        10 => "X",
        50 => "L",
        100 => "C"
    }

    if (self.between?(1, 3))
      return roman[1] * self
    elsif (self.between?(5,8))
      return roman[5] + ("I" * (self - 5))
    elsif(self == 9)
      return "IX"

    elsif(self.between?(10, 39))
      tens = self / 10
      singles = self % 10
      if singles == 0
        return roman[10] * tens
      elsif singles > 0 && singles < 4
        return roman[10] * tens + ("I" * (self - (10 * tens)))
      elsif singles == 4
        return roman[10] * tens + (roman[4])
      elsif singles > 4 && singles < 9
        return roman[10] * tens + ("V" + ("I" * (self - ((10 * tens) + 5))))
      elsif singles == 9
        return roman[10] * tens + (roman[9])
      end

    elsif(self.between?(40, 99))
      if self > 89
        tens = (self / 10) -9
      elsif( self > 49)
        tens = (self / 10) - 5
      else
        tens = (self / 10) - 4
      end

      singles = self % 10
      ninety = "#{roman[10]}#{roman[100]}"
      if self > 89
        prefix = ninety
      elsif self > 49
        prefix = roman[50]
      else
        prefix = "#{roman[10]}#{roman[50]}"
      end
      if singles == 0
        return prefix + (roman[10] * tens)
      elsif singles > 0 && singles <= 3
        return prefix + (roman[10] * tens + ("I" * singles))
      elsif singles == 4
        returnVal = (prefix) + (roman[10] * tens) + (roman[1]) + (roman[5])
        return returnVal
      elsif singles >= 5 && singles < 9
        return prefix + (roman[10] * tens) + ("V" + ("I" * (singles - 5)))
      elsif singles == 9
        return prefix + (roman[10] * tens) + (roman[9])
      end
    elsif(self == 100)
      return roman[100]
    else
      return "IV"
    end
  end
end