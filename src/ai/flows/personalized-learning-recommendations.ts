// src/ai/flows/personalized-learning-recommendations.ts
'use server';

/**
 * @fileOverview This file defines a Genkit flow for providing personalized learning recommendations to users.
 *
 * The flow takes user's skill analyzer results and stated goals as input, and generates personalized recommendations for skills to learn, resources to view, and more.
 *
 * @interface PersonalizedLearningRecommendationsInput - Defines the input schema for the personalized learning recommendations flow.
 * @interface PersonalizedLearningRecommendationsOutput - Defines the output schema for the personalized learning recommendations flow.
 * @function getPersonalizedLearningRecommendations - A function that calls the personalizedLearningRecommendationsFlow.
 */

import {ai} from '@/ai/genkit';
import {z} from 'genkit';

// Define the input schema
const PersonalizedLearningRecommendationsInputSchema = z.object({
  skillAnalyzerResults: z.string().describe('The results from the skill analyzer.'),
  statedGoals: z.string().describe('The stated goals of the user.'),
});
export type PersonalizedLearningRecommendationsInput = z.infer<typeof PersonalizedLearningRecommendationsInputSchema>;

// Define the output schema
const PersonalizedLearningRecommendationsOutputSchema = z.object({
  recommendations: z.string().describe('Personalized learning recommendations for the user.'),
});
export type PersonalizedLearningRecommendationsOutput = z.infer<typeof PersonalizedLearningRecommendationsOutputSchema>;

/**
 * A function that calls the personalizedLearningRecommendationsFlow
 * @param input - The input to the flow.
 * @returns - The output of the flow.
 */
export async function getPersonalizedLearningRecommendations(input: PersonalizedLearningRecommendationsInput): Promise<PersonalizedLearningRecommendationsOutput> {
  return personalizedLearningRecommendationsFlow(input);
}


// Define the prompt
const personalizedLearningRecommendationsPrompt = ai.definePrompt({
  name: 'personalizedLearningRecommendationsPrompt',
  input: {schema: PersonalizedLearningRecommendationsInputSchema},
  output: {schema: PersonalizedLearningRecommendationsOutputSchema},
  prompt: `You are an expert cybersecurity learning recommendation system.

  Based on the user's skill analyzer results and stated goals, provide personalized learning recommendations.

  Skill Analyzer Results: {{{skillAnalyzerResults}}}
  Stated Goals: {{{statedGoals}}}

  Recommendations:
  `,
});

// Define the flow
const personalizedLearningRecommendationsFlow = ai.defineFlow(
  {
    name: 'personalizedLearningRecommendationsFlow',
    inputSchema: PersonalizedLearningRecommendationsInputSchema,
    outputSchema: PersonalizedLearningRecommendationsOutputSchema,
  },
  async input => {
    const {output} = await personalizedLearningRecommendationsPrompt(input);
    return output!;
  }
);
