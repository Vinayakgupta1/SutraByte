"use client";

import React, { useState } from 'react';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import { Alert, AlertDescription } from '@/components/ui/alert';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';
import { useBlockchain } from '@/contexts/BlockchainContext';
import { Shield, Coins, UserPlus, AlertCircle, Loader2, CheckCircle } from 'lucide-react';
import { useToast } from '@/hooks/use-toast';

export const AdminPanel: React.FC = () => {
  const { isAdmin, mintTokens, assignName, loading, error } = useBlockchain();
  const [mintTo, setMintTo] = useState('');
  const [mintAmount, setMintAmount] = useState('');
  const [assignUser, setAssignUser] = useState('');
  const [assignWallet, setAssignWallet] = useState('');
  const [assignNameValue, setAssignNameValue] = useState('');
  const [success, setSuccess] = useState(false);
  const { toast } = useToast();

  if (!isAdmin) {
    return null;
  }

  const handleMint = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!mintTo || !mintAmount) {
      toast({
        title: "Error",
        description: "Please fill in all fields",
        variant: "destructive",
      });
      return;
    }

    if (parseFloat(mintAmount) <= 0) {
      toast({
        title: "Error",
        description: "Amount must be greater than 0",
        variant: "destructive",
      });
      return;
    }

    try {
      setSuccess(false);
      await mintTokens(mintTo, mintAmount);
      setSuccess(true);
      setMintTo('');
      setMintAmount('');
      
      toast({
        title: "Success",
        description: `Successfully minted ${mintAmount} SUTRA tokens to ${mintTo}`,
      });
    } catch (error: any) {
      toast({
        title: "Mint Failed",
        description: error.message,
        variant: "destructive",
      });
    }
  };

  const handleAssignName = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!assignUser || !assignWallet || !assignNameValue) {
      toast({
        title: "Error",
        description: "Please fill in all fields",
        variant: "destructive",
      });
      return;
    }

    try {
      setSuccess(false);
      await assignName(assignUser, assignWallet, assignNameValue);
      setSuccess(true);
      setAssignUser('');
      setAssignWallet('');
      setAssignNameValue('');
      
      toast({
        title: "Success",
        description: `Successfully assigned name ${assignNameValue} to user`,
      });
    } catch (error: any) {
      toast({
        title: "Assignment Failed",
        description: error.message,
        variant: "destructive",
      });
    }
  };

  return (
    <Card className="w-full max-w-2xl mx-auto">
      <CardHeader>
        <CardTitle className="flex items-center gap-2">
          <Shield className="h-5 w-5" />
          Admin Panel
        </CardTitle>
        <CardDescription>
          Manage tokens and user assignments
        </CardDescription>
      </CardHeader>
      <CardContent>
        <Tabs defaultValue="mint" className="w-full">
          <TabsList className="grid w-full grid-cols-2">
            <TabsTrigger value="mint">Mint Tokens</TabsTrigger>
            <TabsTrigger value="assign">Assign Names</TabsTrigger>
          </TabsList>
          
          <TabsContent value="mint" className="space-y-4">
            <form onSubmit={handleMint} className="space-y-4">
              <div className="space-y-2">
                <Label htmlFor="mint-to">Recipient Address</Label>
                <Input
                  id="mint-to"
                  type="text"
                  placeholder="0x..."
                  value={mintTo}
                  onChange={(e) => setMintTo(e.target.value)}
                  disabled={loading}
                />
              </div>
              
              <div className="space-y-2">
                <Label htmlFor="mint-amount">Amount (SUTRA)</Label>
                <Input
                  id="mint-amount"
                  type="number"
                  step="0.01"
                  min="0"
                  placeholder="0.00"
                  value={mintAmount}
                  onChange={(e) => setMintAmount(e.target.value)}
                  disabled={loading}
                />
              </div>

              <Button 
                type="submit" 
                disabled={loading || !mintTo || !mintAmount}
                className="w-full"
              >
                {loading ? (
                  <>
                    <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                    Processing...
                  </>
                ) : (
                  <>
                    <Coins className="mr-2 h-4 w-4" />
                    Mint Tokens
                  </>
                )}
              </Button>
            </form>
          </TabsContent>
          
          <TabsContent value="assign" className="space-y-4">
            <form onSubmit={handleAssignName} className="space-y-4">
              <div className="space-y-2">
                <Label htmlFor="assign-user">User Address</Label>
                <Input
                  id="assign-user"
                  type="text"
                  placeholder="0x..."
                  value={assignUser}
                  onChange={(e) => setAssignUser(e.target.value)}
                  disabled={loading}
                />
              </div>
              
              <div className="space-y-2">
                <Label htmlFor="assign-wallet">Wallet Address</Label>
                <Input
                  id="assign-wallet"
                  type="text"
                  placeholder="0x..."
                  value={assignWallet}
                  onChange={(e) => setAssignWallet(e.target.value)}
                  disabled={loading}
                />
              </div>
              
              <div className="space-y-2">
                <Label htmlFor="assign-name">Name</Label>
                <Input
                  id="assign-name"
                  type="text"
                  placeholder="username"
                  value={assignNameValue}
                  onChange={(e) => setAssignNameValue(e.target.value)}
                  disabled={loading}
                />
              </div>

              <Button 
                type="submit" 
                disabled={loading || !assignUser || !assignWallet || !assignNameValue}
                className="w-full"
              >
                {loading ? (
                  <>
                    <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                    Processing...
                  </>
                ) : (
                  <>
                    <UserPlus className="mr-2 h-4 w-4" />
                    Assign Name
                  </>
                )}
              </Button>
            </form>
          </TabsContent>
        </Tabs>

        {error && (
          <Alert variant="destructive" className="mt-4">
            <AlertCircle className="h-4 w-4" />
            <AlertDescription>{error}</AlertDescription>
          </Alert>
        )}

        {success && (
          <Alert className="mt-4 border-green-200 bg-green-50">
            <CheckCircle className="h-4 w-4 text-green-600" />
            <AlertDescription className="text-green-800">
              Operation completed successfully!
            </AlertDescription>
          </Alert>
        )}
      </CardContent>
    </Card>
  );
};
