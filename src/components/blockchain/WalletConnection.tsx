"use client";

import React from 'react';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Alert, AlertDescription } from '@/components/ui/alert';
import { useBlockchain } from '@/contexts/BlockchainContext';
import { Wallet, Shield, Coins, User, AlertCircle, Loader2 } from 'lucide-react';

export const WalletConnection: React.FC = () => {
  const {
    isConnected,
    account,
    isAdmin,
    balance,
    name,
    connect,
    disconnect,
    loading,
    error
  } = useBlockchain();

  const formatAddress = (address: string) => {
    return `${address.slice(0, 6)}...${address.slice(-4)}`;
  };

  if (!isConnected) {
    return (
      <Card className="w-full max-w-md mx-auto">
        <CardHeader className="text-center">
          <div className="mx-auto mb-4 p-3 bg-primary/10 rounded-full w-fit">
            <Wallet className="h-8 w-8 text-primary" />
          </div>
          <CardTitle>Connect Your Wallet</CardTitle>
          <CardDescription>
            Connect your MetaMask wallet to access SutraByte tokens and features
          </CardDescription>
        </CardHeader>
        <CardContent className="space-y-4">
          {error && (
            <Alert variant="destructive">
              <AlertCircle className="h-4 w-4" />
              <AlertDescription>{error}</AlertDescription>
            </Alert>
          )}
          <Button 
            onClick={connect} 
            disabled={loading}
            className="w-full"
            size="lg"
          >
            {loading ? (
              <>
                <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                Connecting...
              </>
            ) : (
              <>
                <Wallet className="mr-2 h-4 w-4" />
                Connect MetaMask
              </>
            )}
          </Button>
          <p className="text-xs text-muted-foreground text-center">
            Make sure you have MetaMask installed and unlocked
          </p>
        </CardContent>
      </Card>
    );
  }

  return (
    <Card className="w-full max-w-md mx-auto">
      <CardHeader>
        <div className="flex items-center justify-between">
          <CardTitle className="flex items-center gap-2">
            <Wallet className="h-5 w-5" />
            Wallet Connected
          </CardTitle>
          {isAdmin && (
            <Badge variant="secondary" className="flex items-center gap-1">
              <Shield className="h-3 w-3" />
              Admin
            </Badge>
          )}
        </div>
        <CardDescription>
          {name ? `Welcome, ${name}` : `Connected as ${formatAddress(account!)}`}
        </CardDescription>
      </CardHeader>
      <CardContent className="space-y-4">
        <div className="grid grid-cols-2 gap-4">
          <div className="text-center p-3 bg-secondary/50 rounded-lg">
            <div className="flex items-center justify-center gap-1 mb-1">
              <Coins className="h-4 w-4 text-primary" />
              <span className="text-sm font-medium">Balance</span>
            </div>
            <p className="text-lg font-bold">{parseFloat(balance).toFixed(2)} SUTRA</p>
          </div>
          <div className="text-center p-3 bg-secondary/50 rounded-lg">
            <div className="flex items-center justify-center gap-1 mb-1">
              <User className="h-4 w-4 text-primary" />
              <span className="text-sm font-medium">Name</span>
            </div>
            <p className="text-lg font-bold">{name || 'Not set'}</p>
          </div>
        </div>
        
        <div className="pt-2 border-t">
          <Button 
            onClick={disconnect} 
            variant="outline" 
            className="w-full"
          >
            Disconnect
          </Button>
        </div>
      </CardContent>
    </Card>
  );
};
