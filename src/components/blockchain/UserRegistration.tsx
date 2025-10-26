"use client";

import React, { useState } from 'react';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import { Alert, AlertDescription } from '@/components/ui/alert';
import { useBlockchain } from '@/contexts/BlockchainContext';
import { UserPlus, AlertCircle, Loader2, CheckCircle } from 'lucide-react';
import { useToast } from '@/hooks/use-toast';

export const UserRegistration: React.FC = () => {
  const { registerUserName, name, loading, error } = useBlockchain();
  const [userName, setUserName] = useState('');
  const [success, setSuccess] = useState(false);
  const { toast } = useToast();

  const handleRegister = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!userName.trim()) {
      toast({
        title: "Error",
        description: "Please enter a valid name",
        variant: "destructive",
      });
      return;
    }

    if (userName.length < 2) {
      toast({
        title: "Error",
        description: "Name must be at least 2 characters long",
        variant: "destructive",
      });
      return;
    }

    try {
      setSuccess(false);
      await registerUserName(userName.trim());
      setSuccess(true);
      setUserName('');
      
      toast({
        title: "Success",
        description: `Successfully registered name: ${userName}`,
      });
    } catch (error: any) {
      toast({
        title: "Registration Failed",
        description: error.message,
        variant: "destructive",
      });
    }
  };

  if (name) {
    return (
      <Card className="w-full max-w-md mx-auto">
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <UserPlus className="h-5 w-5" />
            Name Registered
          </CardTitle>
          <CardDescription>
            Your name is already registered
          </CardDescription>
        </CardHeader>
        <CardContent>
          <div className="text-center p-4 bg-secondary/50 rounded-lg">
            <p className="text-lg font-semibold">{name}</p>
            <p className="text-sm text-muted-foreground">Registered Name</p>
          </div>
        </CardContent>
      </Card>
    );
  }

  return (
    <Card className="w-full max-w-md mx-auto">
      <CardHeader>
        <CardTitle className="flex items-center gap-2">
          <UserPlus className="h-5 w-5" />
          Register Your Name
        </CardTitle>
        <CardDescription>
          Choose a unique name for your SutraByte account
        </CardDescription>
      </CardHeader>
      <CardContent>
        <form onSubmit={handleRegister} className="space-y-4">
          <div className="space-y-2">
            <Label htmlFor="username">Username</Label>
            <Input
              id="username"
              type="text"
              placeholder="Enter your username"
              value={userName}
              onChange={(e) => setUserName(e.target.value)}
              disabled={loading}
              minLength={2}
              maxLength={20}
            />
            <p className="text-xs text-muted-foreground">
              Choose a unique name (2-20 characters)
            </p>
          </div>

          {error && (
            <Alert variant="destructive">
              <AlertCircle className="h-4 w-4" />
              <AlertDescription>{error}</AlertDescription>
            </Alert>
          )}

          {success && (
            <Alert className="border-green-200 bg-green-50">
              <CheckCircle className="h-4 w-4 text-green-600" />
              <AlertDescription className="text-green-800">
                Name registered successfully!
              </AlertDescription>
            </Alert>
          )}

          <Button 
            type="submit" 
            disabled={loading || !userName.trim()}
            className="w-full"
          >
            {loading ? (
              <>
                <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                Registering...
              </>
            ) : (
              <>
                <UserPlus className="mr-2 h-4 w-4" />
                Register Name
              </>
            )}
          </Button>
        </form>
      </CardContent>
    </Card>
  );
};
