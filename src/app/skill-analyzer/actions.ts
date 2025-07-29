'use server';

import { getPersonalizedLearningRecommendations } from '@/ai/flows/personalized-learning-recommendations';
import { z } from 'zod';

const skillAnalyzerSchema = z.object({
  skillAnalyzerResults: z.string().min(20, "Please provide more details about your current skills and experience for a better recommendation."),
  statedGoals: z.string().min(20, "Please describe your goals in more detail to help us tailor your learning path."),
});

type State = {
  recommendations?: string;
  error?: string | null;
  fieldErrors?: {
    skillAnalyzerResults?: string[];
    statedGoals?: string[];
  }
}

export async function getRecommendations(prevState: State, formData: FormData): Promise<State> {
  const rawData = {
    skillAnalyzerResults: formData.get('skillAnalyzerResults'),
    statedGoals: formData.get('statedGoals'),
  };

  const validation = skillAnalyzerSchema.safeParse(rawData);

  if (!validation.success) {
    return { error: 'Invalid data provided.', fieldErrors: validation.error.flatten().fieldErrors };
  }

  try {
    const result = await getPersonalizedLearningRecommendations(validation.data);
    if(result.recommendations) {
        return { recommendations: result.recommendations, error: null, fieldErrors: {} };
    }
    return { error: 'Could not generate recommendations. Please try again.', fieldErrors: {} };
  } catch (e) {
    console.error(e);
    return { error: 'An unexpected error occurred. Please try again later.', fieldErrors: {} };
  }
}
