'use client';

import { useFormStatus } from 'react-dom';
import { Label } from '@/components/ui/label';
import { Textarea } from '@/components/ui/textarea';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { getRecommendations } from './actions';
import { useEffect, useRef, useActionState } from 'react';
import { useToast } from '@/hooks/use-toast';
import { ArrowRight, Sparkles } from 'lucide-react';

const initialState = {
  recommendations: undefined,
  error: null,
  fieldErrors: {},
};

function SubmitButton() {
  const { pending } = useFormStatus();
  return (
    <Button type="submit" disabled={pending} className="w-full group">
      {pending ? 'Generating...' : 'Get Recommendations'}
      {!pending && <Sparkles className="ml-2 h-5 w-5 transition-transform group-hover:scale-110" />}
    </Button>
  );
}

export function SkillAnalyzerForm() {
  const [state, formAction] = useActionState(getRecommendations, initialState);
  const { toast } = useToast();
  const formRef = useRef<HTMLFormElement>(null);

  useEffect(() => {
    if (state.error) {
      toast({
        title: 'Error',
        description: state.error,
        variant: 'destructive',
      });
    }
    if (state.recommendations) {
      formRef.current?.reset();
    }
  }, [state, toast]);
  

  return (
    <div className="space-y-8">
      <form ref={formRef} action={formAction} className="space-y-6">
        <div className="space-y-2">
          <Label htmlFor="skillAnalyzerResults" className="text-lg font-semibold">
            Your Current Skills & Experience
          </Label>
          <Textarea
            id="skillAnalyzerResults"
            name="skillAnalyzerResults"
            placeholder="e.g., 'I have 2 years of experience as a network admin, comfortable with firewalls and basic scripting. I have a CCNA certification. I want to learn more about cloud security.'"
            rows={5}
            className="text-base"
          />
           {state.fieldErrors?.skillAnalyzerResults && <p className="text-destructive text-sm">{state.fieldErrors.skillAnalyzerResults[0]}</p>}
        </div>
        <div className="space-y-2">
          <Label htmlFor="statedGoals" className="text-lg font-semibold">
            Your Stated Goals
          </Label>
          <Textarea
            id="statedGoals"
            name="statedGoals"
            placeholder="e.g., 'I want to become a penetration tester within the next year. My goal is to get the OSCP certification and work for a top cybersecurity firm.'"
            rows={5}
            className="text-base"
          />
           {state.fieldErrors?.statedGoals && <p className="text-destructive text-sm">{state.fieldErrors.statedGoals[0]}</p>}
        </div>
        <SubmitButton />
      </form>

      {state.recommendations && (
        <Card className="bg-secondary">
          <CardHeader>
            <CardTitle className="flex items-center gap-2 text-2xl">
              <Sparkles className="text-accent" />
              Your Personalized Learning Path
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="prose prose-invert max-w-none">
              <p>{state.recommendations}</p>
            </div>
          </CardContent>
        </Card>
      )}
    </div>
  );
}
