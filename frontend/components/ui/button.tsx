import * as React from 'react';
import { cn } from '@/lib/utils';

export interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'default' | 'secondary' | 'outline' | 'ghost' | 'destructive' | 'tactical' | 'subtle';
  size?: 'default' | 'sm' | 'lg' | 'icon' | 'xs';
}

export const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant = 'default', size = 'default', ...props }, ref) => {
    const variantStyles = {
      default: 'bg-zinc-100 text-zinc-900 hover:bg-zinc-200 border border-zinc-200 shadow-sm',
      secondary: 'bg-zinc-800 text-zinc-100 hover:bg-zinc-700 border border-zinc-700/60 shadow-sm',
      outline: 'bg-transparent text-zinc-200 border border-zinc-800 hover:bg-zinc-800/80 hover:border-zinc-700',
      ghost: 'bg-transparent text-zinc-300 hover:bg-zinc-800/60 hover:text-zinc-100',
      destructive: 'bg-rose-950/80 text-rose-300 border border-rose-800/60 hover:bg-rose-900/80 hover:border-rose-700',
      tactical: 'bg-blue-600 text-white hover:bg-blue-500 border border-blue-500 shadow-sm shadow-blue-900/30',
      subtle: 'bg-zinc-900/80 text-zinc-300 border border-zinc-800 hover:bg-zinc-800/80 hover:text-zinc-100'
    };

    const sizeStyles = {
      default: 'h-9 px-4 py-2 text-xs',
      sm: 'h-8 px-3 text-xs',
      xs: 'h-7 px-2.5 text-[11px]',
      lg: 'h-10 px-5 text-sm',
      icon: 'h-8 w-8 p-0 flex items-center justify-center'
    };

    return (
      <button
        ref={ref}
        className={cn(
          'inline-flex items-center justify-center rounded-lg font-medium transition-all duration-150',
          'focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-zinc-400',
          'disabled:pointer-events-none disabled:opacity-50 select-none active:scale-[0.98]',
          variantStyles[variant],
          sizeStyles[size],
          className
        )}
        {...props}
      />
    );
  }
);

Button.displayName = 'Button';
