import * as React from 'react';
import { cn } from '@/lib/utils';

export interface BadgeProps extends React.HTMLAttributes<HTMLDivElement> {
  variant?: 'default' | 'secondary' | 'outline' | 'success' | 'warning' | 'destructive' | 'tactical' | 'mono';
}

export function Badge({ className, variant = 'default', ...props }: BadgeProps) {
  const variantStyles = {
    default: 'bg-zinc-800 text-zinc-100 border-zinc-700/60',
    secondary: 'bg-zinc-900 text-zinc-300 border-zinc-800',
    outline: 'text-zinc-300 border-zinc-700/60 bg-transparent',
    success: 'bg-emerald-950/70 text-emerald-300 border-emerald-800/60 font-semibold',
    warning: 'bg-amber-950/70 text-amber-300 border-amber-800/60 font-semibold',
    destructive: 'bg-rose-950/70 text-rose-300 border-rose-800/60 font-semibold',
    tactical: 'bg-blue-950/70 text-blue-300 border-blue-800/60 font-semibold',
    mono: 'bg-zinc-900 text-zinc-300 border-zinc-800 font-mono text-[10px]'
  };

  return (
    <div
      className={cn(
        'inline-flex items-center gap-1 rounded-md border px-2 py-0.5 text-xs transition-colors',
        variantStyles[variant],
        className
      )}
      {...props}
    />
  );
}
