Class Trade
    {
    [string]$Symbol
    [datetime]$Time
    [double]$Entry
    [double]$Target
    [double]$Stop
    [double]$TargetOffset
    [double]$StopOffset
    [int]$Shares
    [int]$Risk
    [int]$PositionSize
    [double]$ATR
    [string]$tradeType
    [string]$tradeStatus = "Pending"
    [string]$EntryType
    
    [Void] SetSymbol($Symbol)
        {
        $this.symbol = $Symbol
        }

    [Void] SetTime()
        {
        $this.Time = Get-Date
        }

    [Void] SetEntry($Entry)
        {
        $this.entry = $entry
        }

    [Void] SetTarget($Target)
        {
        $this.Target = $Target
        }
    
    [Void] SetStop($Stop)
        {
        $this.Stop = $Stop
        }
    
    [Void] SetATR($ATR)
        {
        $this.ATR = $ATR
        }

    [Void] SetStatus($Status)
        {
        $this.TradeStatus = $Status
        }

    [Void] SetTradeType($TradeType)
        {
        $this.TradeType = $TradeType
        }

    [Void] SetEntryType($EntryType)
        {
        $this.entryType = $entryType
        }
    
    [Void] SetShares($Shares)
        {
        $this.Shares = $Shares
        }
            
    [Void] CalcRisk()
        {
        $this.Risk = ($this.target - $this.entry) / ($this.entry - $this.stop)
        }
            
    [Void] CalcPositionSize()
        {
        $this.PositionSize = $this.entry * $this.Shares
        }
            
    [Void] CalcOffsets()
        {
        if ($this.tradeType -eq "Buy") 
            {
            $this.TargetOffset = $this.Target - $this.Entry
            $this.StopOffset = $this.Stop - $this.Entry
            }
        elseif ($this.tradeType -eq "Sell")
            {
            $this.TargetOffset = $this.Entry - $this.Target
            $this.StopOffset = $this.Entry - $this.Stop
            }
        else
            {
            "Bad trade type"
            }  
        }
    }


function Create-Trade()
    {
    param
        (
        $Symbol,
        $Entry,
        $Target,
        $Stop,
        $ATR,
        $EntryType,
        $TradeType,
        $Shares
        )

    $trade = New-Object Trade

    $trade.SetTime()
    $trade.SetSymbol($Symbol)
    $trade.SetEntry($Entry)
    $trade.SetTarget($Target)
    $trade.SetStop($Stop)
    $trade.SetATR($ATR)
    $trade.SetEntryType($EntryType)
    $trade.SetTradeType($TradeType)
    $trade.SetShares($Shares)
    $trade.CalcRisk()
    $trade.CalcPositionSize()
    $trade.CalcOffsets()
    
    Return $trade
    }

function Update-TradeStatus($trade,$status)
    {
    $trade.SetStatus($Status)
    
    Return $trade
    }

$trade = Create-Trade `
                -Symbol MSFT `
                -Entry 10.55 `
                -Target 11.00 `
                -Stop 10.30 `
                -ATR 1.4 `
                -EntryType Limit `
                -TradeType Buy `
                -Shares 30

$trade | ft Symbol, Time, TradeStatus, Entry, Target, Stop, TradeType, EntryType, Shares, PositionSize, Risk, ATR, TargetOffset, StopOffset -AutoSize
$trade = Update-TradeStatus $trade "Open"
$trade | ft Symbol, Time, TradeStatus, Entry, Target, Stop, TradeType, EntryType, Shares, PositionSize, Risk, ATR, TargetOffset, StopOffset -AutoSize
$trade = Update-TradeStatus $trade "Closed"
$trade | ft Symbol, Time, TradeStatus, Entry, Target, Stop, TradeType, EntryType, Shares, PositionSize, Risk, ATR, TargetOffset, StopOffset -AutoSize